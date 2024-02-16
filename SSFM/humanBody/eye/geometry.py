from gemc_api_geometry import *

def makeGeometry(configuration):
	irisDisk = MyDetector(name="irisDisk", mother="root")	
	irisDisk.description = "iris disk"
	irisDisk.color       = "00bfff"
	irisDisk.type        = "Tube"
	irisDisk.dimensions = "0.15*mm 0.72*mm 0.005*mm 0*deg 360*deg"
	irisDisk.pos = "-0.005*mm 0.*mm 1.825*mm"
	irisDisk.material   = "G4_WATER"
        irisDisk.visible = "1"
        irisDisk.style = "1"
	irisDisk.sensitivity = "flux"	
	irisDisk.hit_type = "flux"	
	irisDisk.identifiers = "1"	
	print_det(configuration, irisDisk)

        pupilDisk = MyDetector(name="pupilDisk", mother="root")
        pupilDisk.description = "pupil disk"
        pupilDisk.color       = "000000"
        pupilDisk.type        = "Tube"
        pupilDisk.dimensions = "0.*mm 0.15*mm 0.01*mm 0*deg 360*deg"
        pupilDisk.pos = "-0.005*mm 0.*mm 1.825*mm"
        pupilDisk.material   = "G4_WATER"  
        pupilDisk.visible = 1
        pupilDisk.style = 1  
        pupilDisk.hit_type = "flux"
        pupilDisk.identifiers = "1"
	print_det(configuration, pupilDisk)	

        retina = MyDetector(name="retina", mother="root")
        retina.description = "retina"
        retina.color       = "8000802"
        retina.type        = "Sphere"
        retina.dimensions = "1.895*mm 2.*mm 90.*deg 180.*deg 0.*deg 360.*deg"
        retina.pos = "(0., 0., 0.)mm"
#	retina.rotation="(90., 90., -90.)*deg"
	retina.rotation="0.*deg 90.*deg 0.*deg"
        retina.material   = "G4_WATER"        
        retina.visible = 1                   
        retina.style = 1                      
  	retina.sensitivity = "flux"
        retina.hit_type = "flux"              
        retina.identifiers = "1"              
	print_det(configuration, retina)


# first membrane, only half front part
        outerSkinFrontFull = MyDetector(name="outerSkinFrontFull", mother="root")
        outerSkinFrontFull.description = "outerSkin full solid"
        outerSkinFrontFull.color       = "fff5ee2"
        outerSkinFrontFull.type        = "Ellipsoid"
        outerSkinFrontFull.dimensions = "2.0*mm 2.0*mm 2.0*mm  0.*mm 1.825*mm"
        outerSkinFrontFull.pos = "(0., 0., 0.)mm"
        outerSkinFrontFull.material   = "Component"
        outerSkinFrontFull.visible = 0 
        outerSkinFrontFull.style = 1   
        #outerSkinFrontFull.hit_type = "flux" 
        #outerSkinFrontFull.identifiers = "1"  
	#outerSkinFrontFull.sensitivity = "flux"
        print_det(configuration, outerSkinFrontFull)

        outerSkinFrontHole = MyDetector(name="outerSkinFrontHole", mother="root")
        outerSkinFrontHole.description = "outerSkin to be subtracted"
        outerSkinFrontHole.color       = "fff5ee2"
        outerSkinFrontHole.type        = "Ellipsoid"
        outerSkinFrontHole.dimensions = "1.88*mm 1.88*mm 1.88*mm  0.*mm 1.825*mm"
        outerSkinFrontHole.pos = "(0., 0., 0.)mm"
        outerSkinFrontHole.material   = "Component"
        outerSkinFrontHole.visible = 0 
        #outerSkinFrontHole.style = 1   
        #outerSkinFrontHole.hit_type = "flux" 
        #outerSkinFrontHole.identifiers = "1"  
	#outerSkinFrontHole.sensitivity = "flux"
        print_det(configuration, outerSkinFrontHole)

        outerSkinFront = MyDetector(name="outerSkinFront", mother="root")
        outerSkinFront.description = "outerSkin from subtraction"
        outerSkinFront.color       = "fff5ee3"
        outerSkinFront.type        = "Operation: outerSkinFrontFull - outerSkinFrontHole"
        #outerSkinFront.type        = "Ellipsoid"
        #outerSkinFront.dimensions = "1.98*mm 1.98*mm 1.98*mm  0*mm 1.8*mm"
        outerSkinFront.pos = "(0., 0., 0.)mm"
        outerSkinFront.material   = "G4_WATER"
        outerSkinFront.visible = 1 
        outerSkinFront.style = 1   
        outerSkinFront.hit_type = "flux" 
        outerSkinFront.identifiers = "1"  
	outerSkinFront.sensitivity = "flux"
        print_det(configuration, outerSkinFront)

        
# outer membrane, full eyeball except cornea
        scleraFull = MyDetector(name="scleraFull", mother="root")
        scleraFull.description = "outerSkin full solid"
        scleraFull.type        = "Ellipsoid"
        scleraFull.dimensions = "2.02*mm 2.02*mm 2.02*mm  -2.02*mm 1.825*mm"
        scleraFull.pos = "(0., 0., 0.)mm"
        scleraFull.material   = "Component"
        scleraFull.visible = 1 
        scleraFull.style = 1   
        print_det(configuration, scleraFull)

        scleraHole = MyDetector(name="scleraHole", mother="root")
        scleraHole.description = "sclera hole to be subtracted"
        scleraHole.type        = "Ellipsoid"
        scleraHole.dimensions = "2.0*mm 2.0*mm 2.0*mm  -2.0*mm 1.825*mm"
        scleraHole.pos = "(0., 0., 0.)mm"
	scleraHole.material   = "Component"
        scleraHole.visible = 0 
        print_det(configuration, scleraHole)
        sclera = MyDetector(name="sclera", mother="root")
        sclera.description = "outerSkin from subtraction"
        sclera.color       = "ffffff2"
        sclera.type        = "Operation: scleraFull - scleraHole"
        sclera.pos = "(0., 0., 0.)mm"
        sclera.material   = "G4_WATER"
        sclera.visible = 1 
        sclera.style = 1   
        sclera.hit_type = "flux" 
        sclera.identifiers = "4"  
	sclera.sensitivity = "flux"
        print_det(configuration, sclera)

# front cornea
        frontCornea = MyDetector(name="frontCornea", mother="root")
        frontCornea.description = "front cornea skin"
        frontCornea.color       = "afeeee4"
        #outerSkinFront.type        = "Operation: outerSkinFrontFull - outerSkinFrontHole"
        frontCornea.type        = "Ellipsoid"
        frontCornea.dimensions = "2.015*mm 2.015*mm 2.015*mm  1.825*mm 2.15*mm"
        frontCornea.pos = "(0., 0., 0.)mm"
        frontCornea.material   = "G4_WATER"
        frontCornea.visible = 1 
        frontCornea.style = 1   
        frontCornea.hit_type = "flux" 
        frontCornea.identifiers = "1"  
	frontCornea.sensitivity = "flux"
        print_det(configuration, frontCornea)
