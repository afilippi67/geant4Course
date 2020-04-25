from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyFinger() call or  assigned later to the instance variable
	finger = MyDetector(name="flesh", mother="root")	
	finger.description = "finger"
	finger.color       = "FFA07A"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	finger.type        = "Tube"
	finger.dimensions = "0.4*cm 1.*cm 10.*cm 0*deg 360*deg"
        finger.pos = "0.*cm 0.*cm 0.*cm"
        finger.rotation = "90.*deg 0.*deg 0.*deg"                                                
	finger.material   = "G4_MUSCLE_SKELETAL_ICRP"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed

	finger.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	finger.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	finger.sensitivity = "flux"	# Every track through the volume will generate a hit
	finger.hit_type = "flux"		# Every track through the volume will generate a hit
	finger.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, finger)


        bone = MyDetector(name="bone", mother="root")
        bone.description = "bone"
        bone.color       = "FDFEFE"
        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
        # A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
        bone.type        = "Tube"
        bone.dimensions = "0.*cm 0.4*cm 9.*cm 0*deg 360*deg"
	bone.pos = "0.*cm -1.*cm 0.*cm"
        bone.rotation = "90.*deg 0.*deg 0.*deg"
        bone.material   = "G4_BONE_COMPACT_ICRU" # G4_Si is a GEANT4 defined element name
                                                        # When using only built-in materials, a separate materials file is not needed
        bone.visible = 1                    # 1 to display volume with the full geometry, 0 to leave hidden
        bone.style = 1                          # 1 displays volume as a solid, 0 displays as wireframe
        bone.sensitivity = "flux"   # Every track through the volume will generate a hit
        bone.hit_type = "flux"              # Every track through the volume will generate a hit
        bone.identifiers = "1"              # Identifies the detector being hit:  for FLUX detector this is an integer value

        print_det(configuration, bone)
