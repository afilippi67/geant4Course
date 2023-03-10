from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	scintLayer1 = MyDetector(name="scintLayer1", mother="root")	
	scintLayer1.description = "first scintillator layer"
	scintLayer1.color       = "ADD8E6"
	# Box shape dimensions are:  l/2, h/2, w/2
	scintLayer1.type        = "Box"
	scintLayer1.dimensions = "1*m  1.5*m  1.5*cm"
	scintLayer1.pos = "(0., 0., 28.5)*cm"
	scintLayer1.material   = "scintillator"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	scintLayer1.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	scintLayer1.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	scintLayer1.sensitivity = "flux"	# Every track through the volume will generate a hit
	scintLayer1.hit_type = "flux"		# Every track through the volume will generate a hit
	scintLayer1.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, scintLayer1)
	
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	scintLayer2 = MyDetector(name="scintLayer2", mother="root")	
	scintLayer2.description = "second scintillator layer"
	scintLayer2.color       = "ADD8E6"
	# Box shape dimensions are:  l/2, h/2, w/2
	scintLayer2.type        = "Box"
	scintLayer2.dimensions = "1*m  1.5*m  1.5*cm"
	scintLayer2.pos = "(0., 0., 24.9)*cm"
	scintLayer2.material   = "scintillator"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	scintLayer2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	scintLayer2.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	scintLayer2.sensitivity = "flux"	# Every track through the volume will generate a hit
	scintLayer2.hit_type = "flux"		# Every track through the volume will generate a hit
	scintLayer2.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, scintLayer2)
	
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	scintLayer3 = MyDetector(name="scintLayer3", mother="root")	
	scintLayer3.description = "third scintillator layer"
	scintLayer3.color       = "ADD8E6"
	# Box shape dimensions are:  l/2, h/2, w/2
	scintLayer3.type        = "Box"
	scintLayer3.dimensions = "1*m  1.5*m  1.5*cm"
	scintLayer3.pos = "(0., 0., 21.3)*cm"
	scintLayer3.material   = "scintillator"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	scintLayer3.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	scintLayer3.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	scintLayer3.sensitivity = "flux"	# Every track through the volume will generate a hit
	scintLayer3.hit_type = "flux"		# Every track through the volume will generate a hit
	scintLayer3.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, scintLayer3)
	
	#iron
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	ironLayer1 = MyDetector(name="ironLayer1", mother="root")	
	ironLayer1.description = "first iron layer"
	ironLayer1.color       = "8B0000"
	# Box shape dimensions are:  l/2, h/2, w/2
	ironLayer1.type        = "Box"
	ironLayer1.dimensions = "1*m  1.5*m  3*mm"
	ironLayer1.pos = "(0., 0., 26.7)*cm"
	ironLayer1.material   = "G4_Fe"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	ironLayer1.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	ironLayer1.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	ironLayer1.sensitivity = "flux"	# Every track through the volume will generate a hit
	ironLayer1.hit_type = "flux"		# Every track through the volume will generate a hit
	ironLayer1.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, ironLayer1)
	
	#iron
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	ironLayer2 = MyDetector(name="ironLayer2", mother="root")	
	ironLayer2.description = "second iron layer"
	ironLayer2.color       = "8B0000"
	# Box shape dimensions are:  l/2, h/2, w/2
	ironLayer2.type        = "Box"
	ironLayer2.dimensions = "1*m  1.5*m  3*mm"
	ironLayer2.pos = "(0., 0., 23.4)*cm"
	ironLayer2.material   = "G4_Fe"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	ironLayer2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	ironLayer2.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	ironLayer2.sensitivity = "flux"	# Every track through the volume will generate a hit
	ironLayer2.hit_type = "flux"		# Every track through the volume will generate a hit
	ironLayer2.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, ironLayer2)
	
	#iron
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	ironLayer3 = MyDetector(name="ironLayer3", mother="root")	
	ironLayer3.description = "third iron layer"
	ironLayer3.color       = "8B0000"
	# Box shape dimensions are:  l/2, h/2, w/2
	ironLayer3.type        = "Box"
	ironLayer3.dimensions = "1*m  1.5*m  3*mm"
	ironLayer3.pos = "(0., 0., 20.1)*cm"
	ironLayer3.material   = "G4_Fe"	# G4_Si is a GEANT4 defined element name
							# When using only built-in materials, a separate materials file is not needed
	ironLayer3.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	ironLayer3.style = 1			    # 1 displays volume as a solid, 0 displays as wireframe
	ironLayer3.sensitivity = "flux"	# Every track through the volume will generate a hit
	ironLayer3.hit_type = "flux"		# Every track through the volume will generate a hit
	ironLayer3.identifiers = "1"		# Identifies the detector being hit:  for FLUX detector this is an integer value
	print_det(configuration, ironLayer3)
	
	
