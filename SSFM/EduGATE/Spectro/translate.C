#include "TString.h"
#include <iostream>
#include <fstream>

bool startsWith(TString elem,TString sub){
  bool ret = true;
  if(elem.Length()<sub.Length())
    return false;
  for(int i=0;i < sub.Length();i++){
    if(sub.Data()[i]!=elem.Data()[i])
      ret=false;
  }
  return ret; 
}

//"translates" an elements name to an according filename
//ex.: He5 to a2.z5

TString translate(TString el){
  TString elem="";//name of the given element without number
  TString number="";
  
  for(int i=0;i<el.Length();i++){
    TString tmp(el(i,1));
    if(!(tmp.IsDigit())) {
      elem+=el.Data()[i];
    }
    else{
      number+=el.Data()[i];
    }
    
  }
  
  TString result="";

  if(startsWith(elem,"He"))
    result="2";
  else if(startsWith(elem,"Li"))
    result="3";
  else if(startsWith(elem,"Be"))
    result="4";
  else if(startsWith(elem,"Os"))
    result="76";
  else if(startsWith(elem,"Fl"))
    result="114";
  else if(startsWith(elem,"Fe"))
    result="26";
  else if(startsWith(elem,"Ne"))
    result="10";
  else if(startsWith(elem,"Na"))
    result="11";
  else if(startsWith(elem,"Mg"))
    result="12";
  else if(startsWith(elem,"Al"))
    result="13";
  else if(startsWith(elem,"Si"))
    result="14";
  else if(startsWith(elem,"Cl"))
    result="17";
  else if(startsWith(elem,"Ar"))
    result="18";
  else if(startsWith(elem,"Ca"))
    result="20";
  else if(startsWith(elem,"Sc"))
    result="11";
  else if(startsWith(elem,"Ti"))
    result="22";
  else if(startsWith(elem,"Cr"))
    result="24";
  else if(startsWith(elem,"Mn"))
    result="25";
  
  else if(startsWith(elem,"Co"))
    result="27";
  else if(startsWith(elem,"Ni"))
    result="28";
  else if(startsWith(elem,"Cu"))
    result="29";
  else if(startsWith(elem,"Zn"))
    result="30";
  else if(startsWith(elem,"Ga"))
    result="31";
  else if(startsWith(elem,"Ge"))
    result="32";
  else if(startsWith(elem,"As"))
    result="33";
  else if(startsWith(elem,"Se"))
    result="34";
  else if(startsWith(elem,"Br"))
    result="35";
  else if(startsWith(elem,"Kr"))
    result="36";
  else if(startsWith(elem,"Rb"))
    result="37";
  else if(startsWith(elem,"Sr"))
    result="38";
  else if(startsWith(elem,"Zr"))
    result="40";
  else if(startsWith(elem,"Nb"))
    result="41";
  else if(startsWith(elem,"Mo"))
    result="42";
  else if(startsWith(elem,"Tc"))
    result="43";
  else if(startsWith(elem,"Ru"))
    result="44";
  else if(startsWith(elem,"Rh"))
    result="45";
  else if(startsWith(elem,"Pd"))
    result="46";
  else if(startsWith(elem,"Ag"))
    result="47";
  else if(startsWith(elem,"Cd"))
    result="48";
  else if(startsWith(elem,"In"))
    result="49";
  
  else if(startsWith(elem,"Sn"))
    result="50";
  else if(startsWith(elem,"Sb"))
    result="51";
  else if(startsWith(elem,"Te"))
    result="52";
  
  else if(startsWith(elem,"Xe"))
    result="54";
  else if(startsWith(elem,"Cs"))
    result="55";
  else if(startsWith(elem,"Ba"))
    result="56";
  else if(startsWith(elem,"La"))
    result="57";
  else if(startsWith(elem,"Ce"))
    result="58";
  else if(startsWith(elem,"Pr"))
    result="59";
  else if(startsWith(elem,"Nd"))
    result="60";
  else if(startsWith(elem,"Pm"))
    result="61";
  else if(startsWith(elem,"Su"))
    result="62";
  else if(startsWith(elem,"Eu"))
    result="63";
  else if(startsWith(elem,"Gd"))
    result="64";
  else if(startsWith(elem,"Tb"))
    result="65";
  else if(startsWith(elem,"Dy"))
    result="66";
  else if(startsWith(elem,"Ho"))
    result="67";
  else if(startsWith(elem,"Er"))
    result="68";
  else if(startsWith(elem,"Tm"))
    result="69";
  else if(startsWith(elem,"Yb"))
    result="70";
  else if(startsWith(elem,"Lu"))
    result="71";
  else if(startsWith(elem,"Hf"))
    result="72";
  else if(startsWith(elem,"Ta"))
    result="73";
  
  else if(startsWith(elem,"Re"))
    result="75";
  
  else if(startsWith(elem,"Ir"))
    result="77";
  else if(startsWith(elem,"Pt"))
    result="78";
  else if(startsWith(elem,"Au"))
    result="79";
  
  else if(startsWith(elem,"Hg"))
    result="80";
  else if(startsWith(elem,"Tl"))
    result="851";
  else if(startsWith(elem,"Pb"))
    result="82";
  else if(startsWith(elem,"Bi"))
    result="83";
  else if(startsWith(elem,"Po"))
    result="84";
  else if(startsWith(elem,"At"))
    result="85";
  else if(startsWith(elem,"Rn"))
    result="86";
  else if(startsWith(elem,"Fr"))
    result="87";
  else if(startsWith(elem,"Ra"))
    result="88";
  else if(startsWith(elem,"Ac"))
    result="89";
  else if(startsWith(elem,"Th"))
    result="90";
  else if(startsWith(elem,"Pa"))
    result="91";
  
  else if(startsWith(elem,"Np"))
    result="93";
  else if(startsWith(elem,"Pu"))
    result="94";
  else if(startsWith(elem,"Am"))
    result="95";
  else if(startsWith(elem,"Cm"))
    result="96";
  else if(startsWith(elem,"Bk"))
    result="97";
  else if(startsWith(elem,"Cf"))
    result="98";
  else if(startsWith(elem,"Es"))
    result="99";
  else if(startsWith(elem,"Fm"))
    result="100";
  else if(startsWith(elem,"Md"))
    result="101";
  else if(startsWith(elem,"No"))
    result="102";
  else if(startsWith(elem,"Lr"))
    result="103";
  else if(startsWith(elem,"Rf"))
    result="104";
  else if(startsWith(elem,"Db"))
    result="105";
  else if(startsWith(elem,"Sg"))
    result="106";
  else if(startsWith(elem,"Bh"))
    result="107";
  
  else if(startsWith(elem,"Hs"))
    result="108";
  else if(startsWith(elem,"Mt"))
    result="109";
  
  else if(startsWith(elem,"Ds"))
    result="110";
  else if(startsWith(elem,"Rg"))
    result="111";
  else if(startsWith(elem,"Cn"))
    result="112";
  
  else if(startsWith(elem,"Uut"))
    result="113";
  
  else if(startsWith(elem,"Uup"))
    result="115";
  else if(startsWith(elem,"Lv"))
    result="116";
  else if(startsWith(elem,"Uus"))
    result="117";
  else if(startsWith(elem,"UUo"))
    result="118";
  else if(startsWith(elem,"C"))
    result="6";
  else if(startsWith(elem,"U"))
    result="92";
  else if(startsWith(elem,"F"))
    result="9";
  else if(startsWith(elem,"H"))
    result="1";
  else if(startsWith(elem,"B"))
    result="5";
  else if(startsWith(elem,"W"))
    result="74";
  else if(startsWith(elem,"I"))
    result="53";
  else if(startsWith(elem,"O"))
    result="8";
  else if(startsWith(elem,"N"))
    result="7";
  else if(startsWith(elem,"K"))
    result="19";
  else if(startsWith(elem,"P"))
    result="15";
  else if(startsWith(elem,"S"))
    result="16";
  else if(startsWith(elem,"Y"))
    result="39";
  else if(startsWith(elem,"V"))
    result="23";
  else
    result="-1";
  
  result="z"+result+".a"+number;
  return result;
}

bool isElement(TString elem){
  
  TString el=translate(elem);//Uebersetzen des Elements in einen Filename
  
  TString path="RadioactiveDecay3.3/";
  std::ifstream FileTest(path+el);
  bool ret=false;
  
  if(FileTest){
    //	std::cout<<el+" exists."<<std::endl;
    ret=true;
  }
  else{
    //	std::cout<<path+el+" does not exist."<<std::endl;
  }
  
  return ret;
  
  
}

