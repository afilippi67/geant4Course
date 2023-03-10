from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	detector = MyDetector(name="concreteWall", mother="root")	
	detector.description = "concrete wall"
	detector.color       = "DCDCDC"
	# Box shape dimensions are:  l/2, h/2, w/2
	detector.type        = "Box"
	detector.dimensions = "0.5*m  1.*m  0.25*m"
	detector.material   = "G4_CONCRETE"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	detector.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	detector.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	detector.sensitivity = "flux"	# Every track through the volume will generate a hit
	detector.hit_type = "flux"		# Every track through the volume will generate a hit
	detector.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	
	print_det(configuration, detector)
