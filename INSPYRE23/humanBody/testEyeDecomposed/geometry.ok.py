from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	irisDisk = MyDetector(name="irisDisk", mother="root")	
	irisDisk.description = "iris disk"
	irisDisk.color       = "00bfff"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	irisDisk.type        = "Tube"
	irisDisk.dimensions = "0.15*mm 0.71*mm 0.01*mm 0*deg 360*deg"
	irisDisk.pos = "(0., 0., 1.85)mm"
	irisDisk.material   = "G4_WATER"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	irisDisk.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	irisDisk.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	irisDisk.sensitivity = "flux"	# Every track through the volume will generate a hit
	irisDisk.hit_type = "flux"		# Every track through the volume will generate a hit
	irisDisk.identifiers = "1"		# Identifies the irisDisk being hit:  for FLUX irisDisk this is an integer value	
	print_det(configuration, irisDisk)


        pupilDisk = MyDetector(name="pupilDisk", mother="root")
        pupilDisk.description = "pupil disk"
        pupilDisk.color       = "000000"
        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, $
        # A non-zero inner radius will produce a hollow tube.  The angles allow$
        pupilDisk.type        = "Tube"
        pupilDisk.dimensions = "0.*mm 0.15*mm 0.01*mm 0*deg 360*deg"
        pupilDisk.pos = "(0., 0., 1.85)mm"
        pupilDisk.material   = "G4_WATER"        # G4_Si is a GEANT4 defined ele$
                                                        # When using only built$
        pupilDisk.visible = 1                    # 1 to display volume with the $
        pupilDisk.style = 1                          # 1 displays volume as a so$
        pupilDisk.hit_type = "flux"              # Every track through the volum$
        pupilDisk.identifiers = "1"              # Identifies the pupilDisk being$
	print_det(configuration, pupilDisk)	

        retina = MyDetector(name="retina", mother="root")
        retina.description = "retina"
        retina.color       = "8000802"
        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, $
        # A non-zero inner radius will produce a hollow tube.  The angles allow$
        retina.type        = "Sphere"
        retina.dimensions = "1.895*mm 2.*mm 90.*deg 180.*deg 0.*deg 360.*deg"
        retina.pos = "(0., 0., 0.)mm"
#	retina.rotation="(90., 90., -90.)*deg"
	retina.rotation="0.*deg 90.*deg 0.*deg"
        retina.material   = "G4_WATER"        # G4_Si is a GEANT4 defined ele$
                                                        # When using only built$
        retina.visible = 1                    # 1 to display volume with the $
        retina.style = 1                          # 1 displays volume as a so$
  	retina.sensitivity = "flux"
        retina.hit_type = "flux"              # Every track through the volum$
        retina.identifiers = "1"              # Identifies the pupilDisk being$
	print_det(configuration, retina)

#        frontSkinUp = MyDetector(name="frontSkinUp", mother="root")
#        frontSkinUp.description = "frontSkinUp"
#        frontSkinUp.color       = "f0ffff2"
#        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, $
#        # A non-zero inner radius will produce a hollow tube.  The angles allow$
#        frontSkinUp.type        = "Sphere"
#	frontSkinUp.dimensions = "1.895*mm 2.*mm 20.*deg 70.*deg 0.*deg 360.*deg"
#        frontSkinUp.pos = "(0., 0., 0.)mm"
#	frontSkinUp.rotation="0.*deg 90.*deg 0.*deg"
#        frontSkinUp.material   = "G4_WATER"        # G4_Si is a GEANT4 defined ele$
#                                                        # When using only built$
#        frontSkinUp.visible = 1                    # 1 to display volume with the $
#        frontSkinUp.style = 1                          # 1 displays volume as a so$
#        frontSkinUp.hit_type = "flux"              # Every track through the volum$
#        frontSkinUp.identifiers = "1"              # Identifies the pupilDisk being$
#	print_det(configuration, frontSkinUp)
	
#        frontSkinDown = MyDetector(name="frontSkinDown", mother="root")
#        frontSkinDown.description = "frontSkinDown"
#        frontSkinDown.color       = "f0ffff2"
#        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, $
#        # A non-zero inner radius will produce a hollow tube.  The angles allow$
#        frontSkinDown.type        = "Sphere"
#	frontSkinDown.dimensions = "1.895*mm 2.*mm  90.*deg 120.*deg 0.*deg 360.*deg"
#        frontSkinDown.pos = "(0., 0., 0.)mm"
#	frontSkinDown.rotation="0.*deg 90.*deg 0.*deg"
#        frontSkinDown.material   = "G4_WATER"        # G4_Si is a GEANT4 defined ele$
                                                        # When using only built$
#        frontSkinDown.visible = 1                    # 1 to display volume with the $
#        frontSkinDown.style = 1                          # 1 displays volume as a so$
#        frontSkinDown.hit_type = "flux"              # Every track through the volum$
#        frontSkinDown.identifiers = "1"              # Identifies the pupilDisk being$
#	print_det(configuration, frontSkinDown)

#        outerSkin = MyDetector(name="outerSkin", mother="root")
#        outerSkin.description = "outerSkin"
#        outerSkin.color       = "FFFAFA4"
#        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, $
#        # A non-zero inner radius will produce a hollow tube.  The angles allow$
#        outerSkin.type        = "Sphere"
#        outerSkin.dimensions = "2*mm 2.01*mm 0.*deg 180.*deg 0.*deg 180.*deg"
#        outerSkin.pos = "(0., 0., 0.)mm"
#	outerSkin.rotation="(90., 90., -90.)*deg"
#        outerSkin.material   = "G4_WATER"        # G4_Si is a GEANT4 defined ele$
#                                                        # When using only built$
#        outerSkin.visible = 1                    # 1 to display volume with the $
#        outerSkin.style = 1                          # 1 displays volume as a so$
#        outerSkin.hit_type = "flux"              # Every track through the volum$
#        outerSkin.identifiers = "1"              # Identifies the pupilDisk being$
#	print_det(configuration, outerSkin)

        outerSkinFront = MyDetector(name="outerSkinFront", mother="root")
        outerSkinFront.description = "outerSkin"
        outerSkinFront.color       = "fff5ee2"
        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, $
        # A non-zero inner radius will produce a hollow tube.  The angles allow$
        outerSkinFront.type        = "Ellipsoid"
        outerSkinFront.dimensions = "2.01*mm 2.01*mm 2.01*mm  0*mm 1.8*mm"
        outerSkinFront.pos = "(0., 0., 0.)mm"
        outerSkinFront.material   = "G4_WATER"        # G4_Si is a GEANT4 defined ele$
                                                         # When using only built$
        outerSkinFront.visible = 1                    # 1 to display volume with the $
        outerSkinFront.style = 1                          # 1 displays volume as a so$
        outerSkinFront.hit_type = "flux"              # Every track through the volum$
        outerSkinFront.identifiers = "1"              # Identifies the pupilDisk being$
	outerSkinFront.sensitivity = "flux"
 	print_det(configuration, outerSkinFront)
