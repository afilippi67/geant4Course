from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyleadShell() call or  assigned later to the instance variable
	leadShell = MyDetector(name="leadShell", mother="root")	
	leadShell.description = "lead shell"
	leadShell.color       = "808080"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	leadShell.type        = "Sphere"
	leadShell.dimensions = "4.5*cm  5.*cm  0*deg 360*deg 0*deg 180*deg"
	leadShell.material   = "G4_Galactic"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	leadShell.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	leadShell.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	leadShell.sensitivity = "flux"	# Every track through the volume will generate a hit
	leadShell.hit_type = "flux"		# Every track through the volume will generate a hit
	leadShell.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, leadShell)

	# volume fields can be given either as named arguments in the MyleadShell() call or  assigned later to the instance variable
	hollowAir = MyDetector(name="hollowAir", mother="root")	
	hollowAir.description = "hollow air"
	hollowAir.color       = "f0f8ff"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	hollowAir.type        = "Sphere"
	hollowAir.dimensions = "0.*cm  4.5*cm  0*deg 360*deg 0*deg 180*deg"
	hollowAir.material   = "G4_Air"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	hollowAir.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	hollowAir.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	hollowAir.sensitivity = "flux"	# Every track through the volume will generate a hit
	hollowAir.hit_type = "flux"		# Every track through the volume will generate a hit
	hollowAir.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, hollowAir)
