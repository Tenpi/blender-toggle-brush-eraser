bl_info = {
    "name": "Toggle Brush/Eraser",
    "description": "Toggle brush/eraser with b/e keys and other useful bindings.",
    "author": "Moebits",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "category": "Paint"
}

import bpy

addon_keymaps = []

class ToggleBrush(bpy.types.Operator):
    bl_idname = "paint.toggle_brush"
    bl_label = "Toggle Brush"

    def execute(self, context):
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Draw")
        bpy.context.tool_settings.image_paint.brush.blend = "MIX"
        return {"FINISHED"}
    
class ToggleEraser(bpy.types.Operator):
    bl_idname = "paint.toggle_eraser"
    bl_label = "Toggle Eraser"

    def execute(self, context):
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Draw")
        bpy.context.tool_settings.image_paint.brush.blend = "ERASE_ALPHA"
        return {"FINISHED"}
    
class ToggleSoften(bpy.types.Operator):
    bl_idname = "paint.toggle_soften"
    bl_label = "Toggle Soften"

    def execute(self, context):
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Soften")
        return {"FINISHED"}
    
class ToggleSmear(bpy.types.Operator):
    bl_idname = "paint.toggle_smear"
    bl_label = "Toggle Smear"

    def execute(self, context):
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Smear")
        return {"FINISHED"}
    
class ToggleClone(bpy.types.Operator):
    bl_idname = "paint.toggle_clone"
    bl_label = "Toggle Clone"

    def execute(self, context):
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Clone")
        return {"FINISHED"}
    
class ToggleFill(bpy.types.Operator):
    bl_idname = "paint.toggle_fill"
    bl_label = "Toggle Fill"

    def execute(self, context):
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Fill")
        return {"FINISHED"}
    
class ToggleContextMenu(bpy.types.Operator):
    bl_idname = "paint.toggle_context_menu"
    bl_label = "Toggle Context Menu"

    def execute(self, context):
        bpy.ops.wm.call_panel(name="VIEW3D_PT_paint_texture_context_menu")
        return {"FINISHED"}

def register():
    bpy.utils.register_class(ToggleBrush)
    bpy.utils.register_class(ToggleEraser)
    bpy.utils.register_class(ToggleSoften)
    bpy.utils.register_class(ToggleSmear)
    bpy.utils.register_class(ToggleClone)
    bpy.utils.register_class(ToggleFill)
    bpy.utils.register_class(ToggleContextMenu)
        
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name="Image Paint", space_type="EMPTY")
        km1 = km.keymap_items.new(ToggleBrush.bl_idname, "B", "PRESS")
        km2 = km.keymap_items.new(ToggleEraser.bl_idname, "E", "PRESS")
        km3 = km.keymap_items.new(ToggleSoften.bl_idname, "W", "PRESS")
        km4 = km.keymap_items.new(ToggleSmear.bl_idname, "D", "PRESS")
        km5 = km.keymap_items.new(ToggleClone.bl_idname, "C", "PRESS")
        km5 = km.keymap_items.new(ToggleFill.bl_idname, "G", "PRESS")
        km6 = km.keymap_items.new(ToggleContextMenu.bl_idname, "SPACE", "PRESS")
        addon_keymaps.append((km, km1))
        addon_keymaps.append((km, km2))
        addon_keymaps.append((km, km3))
        addon_keymaps.append((km, km4))
        addon_keymaps.append((km, km5))
        addon_keymaps.append((km, km6))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(ToggleBrush)
    bpy.utils.unregister_class(ToggleEraser)
    bpy.utils.unregister_class(ToggleSoften)
    bpy.utils.unregister_class(ToggleSmear)
    bpy.utils.unregister_class(ToggleClone)
    bpy.utils.unregister_class(ToggleFill)
    bpy.utils.unregister_class(ToggleContextMenu)

if __name__ == "__main__":
    register()
