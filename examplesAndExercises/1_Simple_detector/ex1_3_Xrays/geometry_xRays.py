from gemc_api_geometry import *

def makeGeometry(configuration):

#	air = MyDetector(name="air", mother="root")	
#	air.description = "air"
#	air.color       = "FFA07B"
#	air.type        = "Box"
#	air.dimensions = "1*m 1*m 1.*m"
#       air.pos = "0.*cm 0.*cm 0.*cm"
#	air.material   = "G4_AIR"
#	air.visible = 0		      
#	air.style = 1		
#	air.sensitivity = ""	
#	air.hit_type = ""	
#	air.identifiers = "1"	
#	print_det(configuration, air)


	# volume fields can be given either as named arguments in the MyFinger() call or  assigned later to the instance variable
	flesh = MyDetector(name="flesh", mother="root")	
	flesh.description = "flesh"
	flesh.color       = "FFA07A"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	flesh.type        = "Tube"
	flesh.dimensions = "0.5*cm 0.8*cm 5.*cm 0*deg 360*deg"
        flesh.pos = "0.*cm 0.*cm 0.*cm"
        flesh.rotation = "90.*deg 0.*deg 0.*deg"                                                
	flesh.material   = "G4_MUSCLE_SKELETAL_ICRP"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed

	flesh.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	flesh.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	flesh.sensitivity = "flux"	# Every track through the volume will generate a hit
	flesh.hit_type = "flux"		# Every track through the volume will generate a hit
	flesh.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, flesh)


        bone = MyDetector(name="bone", mother="root")
        bone.description = "bone"
        bone.color       = "FDFEFE"
        # Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
        # A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
        bone.type        = "Tube"
        bone.dimensions = "0.*cm 0.5*cm 4.5*cm 0*deg 360*deg"
	bone.pos = "0.*cm -0.5*cm 0.*cm"
        bone.rotation = "90.*deg 0.*deg 0.*deg"
#        bone.material   = "G4_BONE_COMPACT_ICRU" # G4_Si is a GEANT4 defined element name
	bone.material = "G4_Fe"
                                                        # When using only built-in materials, a separate materials file is not needed
        bone.visible = 1                    # 1 to display volume with the full geometry, 0 to leave hidden
        bone.style = 1                          # 1 displays volume as a solid, 0 displays as wireframe
        bone.sensitivity = "flux"   # Every track through the volume will generate a hit
        bone.hit_type = "flux"              # Every track through the volume will generate a hit
        bone.identifiers = "2"              # Identifies the detector being hit:  for FLUX detector this is an integer value

        print_det(configuration, bone)


        film = MyDetector(name="film", mother="root")
        film.description = "film"
        film.color       = "FDFEFE"
        film.type        = "Box"
        film.dimensions = "15.*cm 15*cm 0.1*mm"
	film.pos = "0.*cm 0.*cm 5.*cm"
        film.rotation = "0.*deg 0.*deg 0.*deg"
        film.material   = "G4_PHOTO_EMULSION" 
                                                 
        film.visible = 1                    
        film.style = 1                      
        film.sensitivity = "flux"   
        film.hit_type = "flux"      
        film.identifiers = "3"      

        print_det(configuration, film)
