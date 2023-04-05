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
	body.material = "Component"	# G4_Si is a GEANT4 defined element name
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
	head.material = "Component"	# G4_Si is a GEANT4 defined element name
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
	belly.material = "Component"	# G4_Si is a GEANT4 defined element name
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
	arms.material = "Component"	# G4_Si is a GEANT4 defined element name
	arms.mfield = "no"
	arms.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	arms.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	arms.sensitivity = "flux"	# Every track through the volume will generate a hit
	arms.hit_type = "flux"		# Every track through the volume will generate a hit
	arms.identifiers = "1"		# Identifies the arms being hit:  for FLUX arms this is an integer value	
	print_det(configuration, arms)
	
	hand1 = MyDetector(name="hand1", mother="root")	
	hand1.description = "minion hand1"
	hand1.pos = "0.*cm -85.*cm 10.*cm"
	hand1.rotation = "0*deg 0*deg 0*deg"
	hand1.color = "000000"
	hand1.type = "Sphere"
	hand1.dimensions = "0*cm 12*cm 0.*deg 360*deg 0.*deg 360*deg"
	hand1.material = "banana"	# G4_Si is a GEANT4 defined element name
	hand1.mfield = "no"
	hand1.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	hand1.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	hand1.sensitivity = "flux"	# Every track through the volume will generate a hit
	hand1.hit_type = "flux"		# Every track through the volume will generate a hit
	hand1.identifiers = "1"		# Identifies the hand1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, hand1)
	
	hand2 = MyDetector(name="hand2", mother="root")	
	hand2.description = "minion hand2"
	hand2.pos = "0.*cm 85.*cm 10.*cm"
	hand2.rotation = "0*deg 0*deg 0*deg"
	hand2.color = "000000"
	hand2.type = "Sphere"
	hand2.dimensions = "0*cm 12*cm 0.*deg 360*deg 0.*deg 360*deg"
	hand2.material = "banana"	# G4_Si is a GEANT4 defined element name
	hand2.mfield = "no"
	hand2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	hand2.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	hand2.sensitivity = "flux"	# Every track through the volume will generate a hit
	hand2.hit_type = "flux"		# Every track through the volume will generate a hit
	hand2.identifiers = "1"		# Identifies the hand1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, hand2)
	
        leg1 = MyDetector(name="leg1", mother="root")	
	leg1.description = "minion leg1"
	leg1.pos = "0.*cm 25.*cm -80.*cm"
	leg1.rotation = "0*deg 0*deg 0*deg"
	leg1.color = "4682b4"
	leg1.type = "Tube"
	leg1.dimensions = "0*cm 12*cm 20.*cm 0.*deg 360*deg"
	leg1.material = "Component"	# G4_Si is a GEANT4 defined element name
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
	leg2.material = "Component"	# G4_Si is a GEANT4 defined element name
	leg2.mfield = "no"
	leg2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	leg2.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	leg2.sensitivity = "flux"	# Every track through the volume will generate a hit
	leg2.hit_type = "flux"		# Every track through the volume will generate a hit
	leg2.identifiers = "1"		# Identifies the leg1 being hit:  for FLUX leg1 this is an integer value	
	print_det(configuration, leg2)

        feet1 = MyDetector(name="feet1", mother="root")	
	feet1.description = "minion feet1"
	feet1.pos = "10.*cm 25.*cm -105.*cm"
	feet1.rotation = "0*deg 0*deg 0*deg"
	feet1.color = "000000"
	feet1.type = "Box"
	feet1.dimensions = "20*cm 12*cm 5.*cm"
	feet1.material = "banana"	# G4_Si is a GEANT4 defined element name
	feet1.mfield = "no"
	feet1.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	feet1.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	feet1.sensitivity = "flux"	# Every track through the volume will generate a hit
	feet1.hit_type = "flux"		# Every track through the volume will generate a hit
	feet1.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, feet1)
 
        feet2 = MyDetector(name="feet2", mother="root")	
	feet2.description = "minion feet2"
	feet2.pos = "10.*cm -25.*cm -105.*cm"
	feet2.rotation = "0*deg 0*deg 0*deg"
	feet2.color = "000000"
	feet2.type = "Box"
	feet2.dimensions = "20*cm 12*cm 5.*cm"
	feet2.material = "banana"	# G4_Si is a GEANT4 defined element name
	feet2.mfield = "no"
	feet2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	feet2.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	feet2.sensitivity = "flux"	# Every track through the volume will generate a hit
	feet2.hit_type = "flux"		# Every track through the volume will generate a hit
	feet2.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, feet2)

	google = MyDetector(name="google", mother="root")	
	google.description = "minion google"
	google.pos = "52.*cm 0.*cm 25.*cm"
	google.rotation = "90*deg 90*deg 0*deg"
	google.color = "FFFFFF"
	google.type = "Tube"
	google.dimensions = "0*cm 25*cm 6.*cm 0.*deg 360*deg"
	google.material = "banana"	# G4_Si is a GEANT4 defined element name
	google.mfield = "no"
	google.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	google.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	google.sensitivity = "flux"	# Every track through the volume will generate a hit
	google.hit_type = "flux"		# Every track through the volume will generate a hit
	google.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, google)
	
	googleBorder = MyDetector(name="googleBorder", mother="root")	
	googleBorder.description = "minion googleBorder"
	googleBorder.pos = "52.*cm 0.*cm 25.*cm"
	googleBorder.rotation = "90*deg 90*deg 0*deg"
	googleBorder.color = "808080"
	googleBorder.type = "Tube"
	googleBorder.dimensions = "25*cm 28*cm 6.*cm 0.*deg 360*deg"
	googleBorder.material = "G4_Al"	# G4_Si is a GEANT4 defined element name
	googleBorder.mfield = "no"
	googleBorder.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	googleBorder.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	googleBorder.sensitivity = "flux"	# Every track through the volume will generate a hit
	googleBorder.hit_type = "flux"		# Every track through the volume will generate a hit
	googleBorder.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, googleBorder)
	
	eye = MyDetector(name="eye", mother="root")	
	eye.description = "minion eye"
	eye.pos = "58*cm 0.*cm 25.*cm"
	eye.rotation = "90*deg 90*deg 0*deg"
	eye.color = "a0522d"
	eye.type = "Tube"
	eye.dimensions = "0*cm 10*cm 0.5.*cm 0.*deg 360*deg"
	eye.material = "banana"	# G4_Si is a GEANT4 defined element name
	eye.mfield = "no"
	eye.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	eye.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	eye.sensitivity = "flux"	# Every track through the volume will generate a hit
	eye.hit_type = "flux"		# Every track through the volume will generate a hit
	eye.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, eye)

        mouth = MyDetector(name="mouth", mother="root")	
	mouth.description = "minion mouth"
        mouth.pos = "50*cm 0.*cm 20.*cm"
	mouth.color = "000000"
	mouth.type = "Ellipsoid"
	mouth.dimensions = "15*cm 200*cm 60*cm -60*cm -35*cm"
	mouth.rotation = "0*deg 0*deg 0*deg"
	mouth.material = "Component"	# G4_Si is a GEANT4 defined element name
	mouth.mfield = "no"
	mouth.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	mouth.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	mouth.sensitivity = "flux"	# Every track through the volume will generate a hit
	mouth.hit_type = "flux"		# Every track through the volume will generate a hit
	mouth.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, mouth)

        minionBottom = MyDetector(name="minionBottom", mother="root")	
	minionBottom.description = "minion minionBottom"
	minionBottom.color = "4682b4"
	minionBottom.pos = "0.*cm 0.*cm -54.61*cm"
	minionBottom.type = "Operation:@ belly + leg1"
	minionBottom.material = "Component"	# G4_Si is a GEANT4 defined element name
	minionBottom.mfield = "no"
	minionBottom.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	minionBottom.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	minionBottom.sensitivity = "flux"	# Every track through the volume will generate a hit
	minionBottom.hit_type = "flux"		# Every track through the volume will generate a hit
	minionBottom.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, minionBottom)

        minionBottom2 = MyDetector(name="minionBottom2", mother="root")	
	minionBottom2.description = "minion minionBottom"
	minionBottom2.color = "4682b4"
	minionBottom2.pos = "0.*cm 0.*cm -54.61*cm"
	minionBottom2.type = "Operation:@ minionBottom + leg2"
	minionBottom2.material = "banana"	# G4_Si is a GEANT4 defined element name
	minionBottom2.mfield = "no"
	minionBottom2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	minionBottom2.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	minionBottom2.sensitivity = "flux"	# Every track through the volume will generate a hit
	minionBottom2.hit_type = "flux"		# Every track through the volume will generate a hit
	minionBottom2.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, minionBottom2)

        minionBody = MyDetector(name="minionBody", mother="root")	
	minionBody.description = "minion full body"
	minionBody.color = "ffff99"
	minionBody.pos = "0.*cm 0.*cm 0.*cm"
	minionBody.type = "Operation:@ body - mouth"
	minionBody.material = "Component"	# G4_Si is a GEANT4 defined element name
	minionBody.mfield = "no"
	minionBody.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	minionBody.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	minionBody.sensitivity = "flux"	# Every track through the volume will generate a hit
	minionBody.hit_type = "flux"		# Every track through the volume will generate a hit
	minionBody.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, minionBody)

        minionBody2 = MyDetector(name="minionBody2", mother="root")	
	minionBody2.description = "minion full body part 2"
	minionBody2.color = "ffff99"
	minionBody2.pos = "0.*cm 0.*cm 0.*cm"
	minionBody2.type = "Operation:@ minionBody + head"
	minionBody2.material = "Component"	# G4_Si is a GEANT4 defined element name
	minionBody2.mfield = "no"
	minionBody2.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	minionBody2.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	minionBody2.sensitivity = "flux"	# Every track through the volume will generate a hit
	minionBody2.hit_type = "flux"		# Every track through the volume will generate a hit
	minionBody2.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, minionBody2)
	
	minionBody3 = MyDetector(name="minionBody3", mother="root")	
	minionBody3.description = "minion full body part 3"
	minionBody3.color = "ffff99"
	minionBody3.pos = "0.*cm 0.*cm 0.*cm"
	minionBody3.type = "Operation:@ minionBody2 + arms"
	minionBody3.material = "banana"	# G4_Si is a GEANT4 defined element name
	minionBody3.mfield = "no"
	minionBody3.visible = 1			# 1 to display volume with the full geometry, 0 to leave hidden
	minionBody3.style = 1			# 1 displays volume as a solid, 0 displays as wireframe
	minionBody3.sensitivity = "flux"	# Every track through the volume will generate a hit
	minionBody3.hit_type = "flux"		# Every track through the volume will generate a hit
	minionBody3.identifiers = "1"		# Identifies the feet1 being hit:  for FLUX feet1 this is an integer value	
	print_det(configuration, minionBody3)
	
