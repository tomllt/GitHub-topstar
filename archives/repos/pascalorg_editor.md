# Pascal Editor

A 3D building editor built with React Three Fiber and WebGPU.



https://github.com/user-attachments/assets/8b50e7cf-cebe-4579-9cf3-8786b35f7b6b



## Repository Architecture

This is a Turborepo monorepo with three main packages:

```
editor-v2/
├── apps/
│   └── editor/          # Next.js application
├── packages/
│   ├── core/            # Schema definitions, state management, systems
│   └── viewer/          # 3D rendering components
```

### Separation of Concerns

| Package | Responsibility |
|---------|---------------|
| **@pascal-app/core** | Node schemas, scene state (Zustand), systems (geometry generation), spatial queries, event bus |
| **@pascal-app/viewer** | 3D rendering via React Three Fiber, default camera/controls, post-processing |
| **apps/editor** | UI components, tools, custom behaviors, editor-specific systems |

The **viewer** renders the scene with sensible defaults. The **editor** extends it with interactive tools, selection management, and editing capabilities.

### Stores

Each package has its own Zustand store for managing state:

| Store | Package | Responsibility |
|-------|---------|----------------|
| `useScene` | `@pascal-app/core` | Scene data: nodes, root IDs, dirty nodes, CRUD operations. Persisted to IndexedDB with undo/redo via Zundo. |
| `useViewer` | `@pascal-app/viewer` | Viewer state: current selection (building/level/zone IDs), level display mode (stacked/exploded/solo), camera mode. |
| `useEditor` | `apps/editor` | Editor state: active tool, structure layer visibility, panel states, editor-specific preferences. |

**Access patterns:**

```typescript
// Subscribe to state changes (React component)
const nodes = useScene((state) => state.nodes)
const levelId = useViewer((state) => state.selection.levelId)
const activeTool = useEditor((state) => state.tool)

// Access state outside React (callbacks, systems)
const node = useScene.getState().nodes[id]
useViewer.getState().setSelection({ levelId: 'level_123' }

... (truncated)