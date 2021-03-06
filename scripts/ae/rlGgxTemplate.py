import pymel.core as pm
from mtoa.ui.ae.shaderTemplate import ShaderAETemplate


class AErlGgxTemplate(ShaderAETemplate):

    def setup(self):
        # Add the shader swatch to the AE
        self.addSwatch()
        self.beginScrollLayout()

        self.beginLayout("Diffuse", collapse=False)
        self.addControl("KdColor", label="Color")
        self.addControl("Kd", label="Weight")
        self.addControl("diffuseRoughness", label="Roughness")
        self.endLayout()

        self.beginLayout("Specular", collapse=False)
        self.addControl("KsColor", label="Color")
        self.addControl("Ks", label="Weight")
        self.addControl("specularRoughness", label="Roughness")
        self.addControl("anisotropic")
        self.addControl("ior", label="IOR")
        self.endLayout()

        self.beginLayout("Refract", collapse=False)
        self.addControl("KtColor", label="Color")
        self.addControl("Kt", label="Weight")
        self.endLayout()

        self.beginLayout("Opacity", collapse=True)
        self.addControl("opacity", label="Weight")
        self.addControl("opacity_color", label="Color")
        self.endLayout()

        self.addBumpLayout()
        self.addAOVLayout(aovReorder=["direct_diffuse", "direct_specular",
            "refraction", "indirect_diffuse", "indirect_specular"])

        # include/call base class/node attributes
        pm.mel.AEdependNodeTemplate(self.nodeName)

        # Add Section for the extra controls not displayed before
        self.addExtraControls()
        self.endScrollLayout()
