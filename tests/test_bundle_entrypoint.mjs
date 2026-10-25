import assert from 'node:assert/strict'
import { apply, inject, name } from '../index.js'

const registered = []
const disposers = []
const context = {
  skills: {
    register(skill) {
      registered.push(skill)
      return () => disposers.push(skill.name)
    },
  },
  effect(factory, label) {
    assert.equal(label, 'dsh-impeccableme Skills')
    const iterator = factory()
    let step = iterator.next()
    while (!step.done) {
      if (typeof step.value === 'function') disposers.push(step.value)
      step = iterator.next()
    }
  },
}

assert.equal(name, 'dsh-impeccableme')
assert.deepEqual(inject, ['skills'])
apply(context)
assert.equal(registered.length, 8)
assert.deepEqual(registered.map((skill) => skill.name).sort(), [
  'frontend-engineering',
  'interface-blueprint',
  'project-context',
  'system-documentation',
  'ui-quality-audit',
  'ux-content',
  'visual-refinement',
  'workspace-operator',
])
for (const skill of registered) {
  assert.ok(skill.description.length > 0, skill.name)
  assert.ok(skill.content.length > 100, skill.name)
  assert.equal(skill.source, 'bundled')
  assert.match(skill.path, /\.dsh[\\/]skills[\\/].+[\\/]SKILL\.md$/)
}
assert.equal(disposers.length, 8)
console.log('Bundle entrypoint test: PASS (8 registered Skills)')
