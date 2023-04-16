from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	waterbox = MyDetector(name="waterbox", mother="root")	
	waterbox.description = "waterbox container"
	waterbox.color       = "7fffd42"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	waterbox.type        = "Box"
	waterbox.dimensions = "10*cm 10*cm 10*cm"
	waterbox.pos = "0.*cm 0.*cm 0.*cm"
	waterbox.material   = "G4_WATER"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	waterbox.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	waterbox.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	#waterbox.sensitivity = "flux"	# Every track through the volume will generate a hit
	#waterbox.hit_type = "flux"		# Every track through the volume will generate a hit
	waterbox.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, waterbox)
	
	
	leadDet = MyDetector(name="leadDet", mother="waterbox")	
	leadDet.description = "lead detector"
	leadDet.color       = "ffff00"
	leadDet.type        = "Box"
	leadDet.dimensions = "3*cm 3*cm 3*cm"
	leadDet.pos = "2*cm 2*cm 3*cm"
	leadDet.material   = "G4_Pb"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	leadDet.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	leadDet.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	leadDet.sensitivity = "flux"	# Every track through the volume will generate a hit
	leadDet.hit_type = "flux"		# Every track through the volume will generate a hit
	leadDet.identifiers = "2"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, leadDet)
	
	
	screen = MyDetector(name="screen", mother="root")	
	screen.description = "screen detector"
	screen.color       = "c0c0c0"
	screen.type        = "Box"
	screen.dimensions = "10*cm 10*cm 0.2*cm"
	screen.pos = "0*cm 0*cm -20*cm"
	screen.material   = "G4_Pb"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	screen.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	screen.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	screen.sensitivity = "flux"	# Every track through the volume will generate a hit
	screen.hit_type = "flux"		# Every track through the volume will generate a hit
	screen.identifiers = "3"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, screen)
