from gemc_api_geometry import *

def makeGeometry(configuration):
	# volume fields can be given either as named arguments in the MyDetector() call or  assigned later to the instance variable
	body = MyDetector(name="body", mother="root")	
	body.description = "minion body"
	body.pos = "0.*cm 0.*cm 0.*cm"
	body.rotation = "0*deg 0*deg 0*deg"
	body.color = "ffff99"
	body.type = "Tube"
	body.dimensions = "0.*cm 50.*cm 54.6*cm 0*deg 360*deg"
	body.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	body.mfield = "no"
	body.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	body.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	body.sensitivity = "flux"	# Every track through the volume will generate a hit
	body.hit_type = "flux"		# Every track through the volume will generate a hit
	body.identifiers = "1"		# Identifies the body being hit:  for FLUX body this is an integer value	
	print_det(configuration, body)

        head = MyDetector(name="head", mother="root")	
	head.description = "minion head"
	head.pos = "0.*cm 0.*cm 54.61*cm"
	head.rotation = "0*deg 0*deg 0*deg"
	head.color = "ffff00"
	head.type = "Ellipsoid"
	head.dimensions = "50.*cm 50.*cm 35*cm 0.*cm 35.*cm"
	head.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	head.mfield = "no"
	head.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	head.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	head.sensitivity = "flux"	# Every track through the volume will generate a hit
	head.hit_type = "flux"		# Every track through the volume will generate a hit
	head.identifiers = "1"		# Identifies the head being hit:  for FLUX head this is an integer value	
	print_det(configuration, head)

        belly = MyDetector(name="belly", mother="root")	
	belly.description = "minion belly"
	belly.pos = "0.*cm 0.*cm -54.61*cm"
	belly.rotation = "0*deg 0*deg 0*deg"
	belly.color = "4682b4"
	belly.type = "Ellipsoid"
	belly.dimensions = "50*cm 50*cm 35.*cm -35*cm 0.*cm"
	belly.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	belly.mfield = "no"
	belly.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	belly.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	belly.sensitivity = "flux"	# Every track through the volume will generate a hit
	belly.hit_type = "flux"		# Every track through the volume will generate a hit
	belly.identifiers = "1"		# Identifies the belly being hit:  for FLUX belly this is an integer value	
	print_det(configuration, belly)

        
        arms = MyDetector(name="arms", mother="root")	
	arms.description = "minion arms"
	arms.pos = "0.*cm 0.*cm 10.*cm"
	arms.rotation = "90*deg 0*deg 0*deg"
	arms.color = "ffff00"
	arms.type = "Tube"
	arms.dimensions = "0.*cm 12.*cm 80*cm 0.*deg 360.*deg"
	arms.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	arms.mfield = "no"
	arms.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	arms.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	arms.sensitivity = "flux"	# Every track through the volume will generate a hit
	arms.hit_type = "flux"		# Every track through the volume will generate a hit
	arms.identifiers = "1"		# Identifies the arms being hit:  for FLUX arms this is an integer value	
	print_det(configuration, arms)
	
	
        leg1 = MyDetector(name="leg1", mother="root")	
	leg1.description = "minion leg1"
	leg1.pos = "0.*cm 25.*cm -80.*cm"
	leg1.rotation = "0*deg 0*deg 0*deg"
	leg1.color = "4682b4"
	leg1.type = "Tube"
	leg1.dimensions = "0*cm 12*cm 20.*cm 0.*deg 360*deg"
	leg1.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	leg1.mfield = "no"
	leg1.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	leg1.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	leg1.sensitivity = "flux"	# Every track through the volume will generate a hit
	leg1.hit_type = "flux"		# Every track through the volume will generate a hit
	leg1.identifiers = "1"		# Identifies the leg1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, leg1)

	leg2 = MyDetector(name="leg2", mother="root")	
	leg2.description = "minion leg2"
	leg2.pos = "0.*cm -25.*cm -80.*cm"
	leg2.rotation = "0*deg 0*deg 0*deg"
	leg2.color = "4682b4"
	leg2.type = "Tube"
	leg2.dimensions = "0*cm 12*cm 20.*cm 0.*deg 360*deg"
	leg2.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	leg2.mfield = "no"
	leg2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	leg2.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	leg2.sensitivity = "flux"	# Every track through the volume will generate a hit
	leg2.hit_type = "flux"		# Every track through the volume will generate a hit
	leg2.identifiers = "1"		# Identifies the leg1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, leg2)


	google = MyDetector(name="google", mother="root")	
	google.description = "minion google"
	google.pos = "52.*cm 0.*cm 25.*cm"
	google.rotation = "90*deg 90*deg 0*deg"
	google.color = "FFFFFF"
	google.type = "Tube"
	google.dimensions = "0*cm 25*cm 5.*cm 0.*deg 360*deg"
	google.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	google.mfield = "no"
	google.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	google.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	google.sensitivity = "flux"	# Every track through the volume will generate a hit
	google.hit_type = "flux"		# Every track through the volume will generate a hit
	google.identifiers = "1"		# Identifies the leg1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, google)
	
	eye = MyDetector(name="eye", mother="root")	
	eye.description = "minion eye"
	eye.pos = "58*cm 0.*cm 25.*cm"
	eye.rotation = "90*deg 90*deg 0*deg"
	eye.color = "a0522d"
	eye.type = "Tube"
	eye.dimensions = "0*cm 10*cm 0.5.*cm 0.*deg 360*deg"
	eye.material = "G4_Si"	# G4_Si is a GEANT4 defined element name
	eye.mfield = "no"
	eye.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	eye.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	eye.sensitivity = "flux"	# Every track through the volume will generate a hit
	eye.hit_type = "flux"		# Every track through the volume will generate a hit
	eye.identifiers = "1"		# Identifies the leg1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, eye)
