#include "translate.C"
#include <iostream>
#include <fstream>

bool isElement(TString elem){
	
	TString el=translate(elem);//Uebersetzen des Elements in einen Filename

	TString path="RadioactiveDecay3.3/";
	std::ifstream FileTest(path+el);
	bool ret=false;
	if(FileTest){
		std::cout<<el+" exists."<<std::endl;
		ret=true;
	}
	else{
		std::cout<<path+el+" does not exist."<<std::endl;
	}
	
	return ret;


}
