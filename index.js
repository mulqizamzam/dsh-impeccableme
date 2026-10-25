import { readdirSync, readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

export const name = 'dsh-impeccableme'
export const inject = ['skills']

const packageRoot = dirname(fileURLToPath(import.meta.url))
const skillsRoot = join(packageRoot, '.dsh', 'skills')

function parseSkill(source, skillPath) {
  const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/)
  if (!match) throw new Error(`Missing YAML frontmatter in ${skillPath}`)

  const metadata = Object.create(null)
  for (const line of match[1].split(/\r?\n/)) {
    const trimmed = line.trim()
    if (!trimmed || trimmed.startsWith('#')) continue
    const colon = trimmed.indexOf(':')
    if (colon < 1) throw new Error(`Invalid frontmatter line in ${skillPath}: ${line}`)
    const key = trimmed.slice(0, colon).trim()
    let value = trimmed.slice(colon + 1).trim()
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1)
    }
    if (!value || Object.hasOwn(metadata, key)) throw new Error(`Invalid metadata field "${key}" in ${skillPath}`)
    metadata[key] = value
  }

  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(metadata.name ?? '')) {
    throw new Error(`Invalid Skill name in ${skillPath}`)
  }
  if (typeof metadata.description !== 'string' || !metadata.description.trim()) {
    throw new Error(`Missing Skill description in ${skillPath}`)
  }

  return {
    name: metadata.name,
    description: metadata.description,
    source: 'bundled',
    path: skillPath,
    content: source.slice(match[0].length).trimStart(),
  }
}

function loadSkills() {
  return readdirSync(skillsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .sort((left, right) => left.name.localeCompare(right.name))
    .map((entry) => {
      const skillPath = join(skillsRoot, entry.name, 'SKILL.md')
      const source = readFileSync(skillPath, 'utf8')
      const skill = parseSkill(source, skillPath)
      if (skill.name !== entry.name) {
        throw new Error(`Skill name "${skill.name}" does not match directory "${entry.name}"`)
      }
      return skill
    })
}

export function apply(ctx) {
  const skills = loadSkills()
  ctx.effect(function* registerBundledSkills() {
    for (const skill of skills) {
      yield ctx.skills.register(skill)
    }
  }, 'dsh-impeccableme Skills')
}
