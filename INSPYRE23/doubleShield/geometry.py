from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	leadShield = MyDetector(name="lead Shield", mother="root")	
	leadShield.description = "leadShield"
	leadShield.color       = "696969"
	# Box shape dimensions are:  l/2, h/2, w/2
	leadShield.type        = "Box"
	leadShield.dimensions = "0.25*m  0.4*m  2.5.*mm"
	leadShield.pos = "-0.25.*m 0.4*mm 30*cm"
	leadShield.material   = "G4_Pb"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	leadShield.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	leadShield.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	leadShield.sensitivity = "flux"	# Every track through the volume will generate a hit
	leadShield.hit_type = "flux"		# Every track through the volume will generate a hit
	leadShield.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
        print_det(configuration, leadShield)

        # volume fields can be given either as named arguments in the MyDetecto$
        aluminumShield = MyDetector(name="aluminum Shield", mother="root")
        aluminumShield.description = "aluminumShield"
        aluminumShield.color       = "c0c0c0"
        # Box shape dimensions are:  l/2, h/2, w/2
        aluminumShield.type        = "Box"
        aluminumShield.dimensions = "0.25*m  0.4*m  2.5.*mm"
        aluminumShield.pos = "0.25.*m 0.4*mm 30*cm"
        aluminumShield.material   = "G4_Al" # G4_Si is a GEANT4 defined element name
                                                        # When using only built$
        aluminumShield.visible = 1                  # 1 to display volume with the $
        aluminumShield.style = 1                        # 1 displays volume as a so$
        aluminumShield.sensitivity = "flux" # Every track through the volume will g$
        aluminumShield.hit_type = "flux"            # Every track through the volum$
        aluminumShield.identifiers = "1"            # Identifies the detector being$
        print_det(configuration, aluminumShield)


