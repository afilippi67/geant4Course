from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyburningAppendix() call or  assigned later to the instance variable
	burningAppendix = MyDetector(name="burningAppendix", mother="root")	
	burningAppendix.description = "appendix with baryum sulphate"
	burningAppendix.color       = "fffaf0"
	# Tube shape dimensions are:  inner_radius, outer_radius, half-length, starting_angle, total angle
	# A non-zero inner radius will produce a hollow tube.  The angles allow for an angular cut in the cross section
	burningAppendix.type        = "Sphere"
	burningAppendix.dimensions = "0.*cm 0.25*cm 0.*deg 360*deg 0.*deg 180.*deg"
	burningAppendix.pos = "1*cm -6.5*cm 4.*cm"
	burningAppendix.material   = "baryumSulphate"    # When using only built-in materials, a separate materials file is not needed
	burningAppendix.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	burningAppendix.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	burningAppendix.sensitivity = "flux"	# Every track through the volume will generate a hit
	burningAppendix.hit_type = "flux"		# Every track through the volume will generate a hit
	burningAppendix.identifiers = "1"		# Identifies the burningAppendix being hit:  for FLUX detector this is an integer value 
	print_det(configuration, burningAppendix)

        film = MyDetector(name="film", mother="root")
        film.description = "film"
        film.color       = "FDFEFE"
        film.type        = "Box"
        film.dimensions = "15.*cm 15*cm 0.1*mm"
        film.pos = "0.*cm 0.*cm -5.*cm"
        film.rotation = "0.*deg 0.*deg 0.*deg"
        film.material   = "G4_PHOTO_EMULSION"                                                  
        film.visible = 1                    
        film.style = 1                      
        film.sensitivity = "flux"   
        film.hit_type = "flux"      
        film.identifiers = "2" 
	
	     
        print_det(configuration, film)
