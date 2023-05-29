from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	detector = MyDetector(name="burningAppendix", mother="root")	
	detector.description = "appendix with baryum sulphate"
	detector.color       = "fffaf0"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	detector.type        = "Sphere"
	detector.dimensions = "0.*cm 0.25*cm 0.*deg 360*deg 0.*deg 180.*deg"
	detector.pos = "1*cm -6.5*cm 4.*cm"
	detector.material   = "baryumSulphate"    # When using only built-in materials, a separate materials file is not needed
	detector.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	detector.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	detector.sensitivity = "flux"	# Every track through the volume will generate a hit
	detector.hit_type = "flux"		# Every track through the volume will generate a hit
	detector.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	
	print_det(configuration, detector)
