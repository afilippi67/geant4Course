
// GenerateGateConfiguration.C
// This macro allows the configuration of a GATE simulation.
// The user is allowed to configure various simulation parameters 
// by choosing between predefined options set in Gamma_Camera.txt.
// The result is written into the GATE macro file "configuration.mac",
//  which is called by the main GATE macro.


// Das TextFile ist in der Form
// Bezeichner : arg1; arg2; arg3; arg4; arg5;
// anzulegen, Argumente ohne ";" werden ignoriert
// Zeilen nach dem Zeichen "-" werden nicht aufgefuehrt, aber eingelesen


// Die Output Datei hat die Form pro Zeile:
// /control/alias/ Bezeichner (ausgewaehltes Element)
// Der Alias wird von Gate (im "UsedMacro") verarbeitet und dort gesetzt



#include <TApplication.h>
#include <TGClient.h>
#include <TGButton.h>
#include <TGListBox.h>
#include <TList.h>
#include <TGComboBox.h>
#include <vector>
#include <TGLabel.h>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <Riostream.h>
#include "translate.C"


using namespace std;
class GateConfiguration : public TGMainFrame {
  
private:
  vector<TGComboBox*> 		fCombo;  //Dropdownmenues, werden aus datei eingelesen
  TGCheckButton       		*fCheckMulti;
  TList               		*fSelected;   
  vector<string*>			used;
  vector<TGHorizontalFrame*> 	hframes;
  vector<TGLabel*>		labels;
  int 				numCombo;//anzahl der verwendeten menuepunkten (also anzahl der menues)
  int				border; //nummer der Trennzeile
  char				* config;
  vector<string>			exceptions;//labels, die nicht in configuration.mac geschrieben werden sollen
  vector<string>			additional;//Dateien, die zusaetzlich durchsucht werden sollen
  
  
  
  
public:
  GateConfiguration(const TGWindow *p, UInt_t w, UInt_t h, char* conf);
  virtual ~GateConfiguration();
  void DoExit();
  void GenerateConfigFile();
  void Save();
  void showDetails();
  void checkForDependencies();
  void insertLabel(string);
  void searchFile(const char*);
  
  ClassDef(GateConfiguration, 0) //fuegt die klasse bei root hinzu, 0 ist die version-ID
};

void GateConfiguration::insertLabel(string name){ //nur nach der Initialisierung der Klasse brauchbar !
	string line;
	int found=0;
	int numParameters=0;
	bool isUsed=false;
	for(int k=0; k<numCombo;k++){
		if(strcmp(used.at(k)->c_str(),name.c_str())==0){ 
			isUsed=true;
			//cout<<used.at(k)->c_str()<<endl;
		}			
	}
	for(unsigned int l=0;l<sizeof(exceptions)/sizeof(exceptions[0]);l++){
		if(strcmp(exceptions[l].c_str(),name.c_str())==0){ 
			isUsed=true;
			//cout<<used.at(k)->c_str()<<endl;
		}
	}
	//cout<<name<<" "<<isUsed<<endl;						
	if(!isUsed){//nachschauen, ob es StandardParameter gibt
	  
	  hframes.push_back(new TGHorizontalFrame(this, 350, 20, kLHintsExpandX));
	  
	  fCombo.push_back(new TGComboBox(hframes[numCombo], 100));
	  labels.push_back(new TGLabel(hframes[numCombo],new TGString(name.c_str())));
	  fCombo.at(numCombo)->Resize(300, 20);	
	  
	  hframes.at(numCombo)->AddFrame(labels.at(numCombo),new TGLayoutHints(kLHintsExpandX, 5, 5, 3, 4));
	  hframes.at(numCombo)->AddFrame(fCombo.at(numCombo), new TGLayoutHints(kLHintsExpandX , 5, 5, 5, 5));
	  AddFrame(hframes.at(numCombo), new TGLayoutHints(kLHintsExpandX, 2, 2, 5, 1));
	  fCombo.at(numCombo)->EnableTextInput(false);
	  
	  used.push_back(new string(name.c_str()));
	  
	  Resize(GetDefaultSize());
	  MapSubwindows();
	  MapWindow();
	  ifstream configIn(config);
	  //cout << " border value " << border << endl;
	  for(int k=0;k<border;k++){
	    getline(configIn, line);//Zeilen vor border auslesen
	  }
	  bool b = false;//gibt an, ob ein menpkt gefunden wurde
	  while(getline(configIn,line)){//auslesen nach border

	    //cout << "line " << line << endl; // qui legge tutta la lista 
	    found=line.find(":");
	    char al[100];
	    line.copy(al,found,0);
	    al[found]='\0';
		  
	    if(strcmp(al,name.c_str())==0){//das gesuchte label hat menpkt
	      found = 0;
	      numParameters=0;
	      b=true;
	      while(found!=-1){
		found=line.find(";",found+1);
		numParameters++;
	      };
	      numParameters--;
	      //cout<<numParameters<<endl;
	      found=line.find(":");
	      for (int j=0; j<numParameters; j++) {
		
		int start=found+1;
		found=line.find(";",start);
		line.copy(al,found-start,start);
		//cout<<al<<endl;
		al[found-start]='\0';
		if(al[0] == '?')
		  fCombo[numCombo]->EnableTextInput(true);
		else
		  fCombo[numCombo]->AddEntry(al, j+1);
	      }
	      fCombo[numCombo]->Select(1);
	    }
	    
	  }
	  if(!b){	 
	    fCombo[numCombo]->AddEntry("", 1);
	    fCombo[numCombo]->EnableTextInput(true);
	  }
	  configIn.close();
	  numCombo++;
	}
}

void GateConfiguration::GenerateConfigFile(){	
	
  ofstream fout("configuration.mac");
	
  for (int i=0; i<numCombo; i++) {
		
    if (fCombo[i]->GetSelected()!=-1) {
      TGLBEntry *entry=fCombo[i]->GetSelectedEntry();
      const char* value =((TGTextLBEntry*)entry)->GetText()->GetString();

      //cout << ((TGTextLBEntry*)entry)->GetText()->GetString() << " " << i << endl;
      if(!((TGTextLBEntry*)entry)->GetText()->IsWhitespace()){
	if(strcmp(labels[i]->GetText()->GetString(), "Type in isotope, e.g. Na22")==0){
	  if(isElement(value)) {
	    cout<<"/control/alias SourceType ion_"<<value<<endl;
	    fout<<"/control/alias SourceType ion_"<<value<<endl;
	    TString s = translate(value);
	    TString ion_z_val="";
	    TString ion_a_val="";
	    TString tmp;
	    bool a = true;
	    for(int k=1;k<s.Length();k++){
	      tmp=s(k,1);
	      if(tmp.IsDigit() && a){
		ion_z_val+=s.Data()[k];
	      }
	      else if(tmp.IsDigit() && !a){
		ion_a_val+=s.Data()[k];
	      }
	      else if(a){
		a=false;
	      }
	    }
	    cout<<"/control/alias "<<"Ion_A_val"<<" "<<ion_a_val<<endl;
	    fout<<"/control/alias "<<"Ion_A_val"<<" "<<ion_a_val<<endl;
	    
	    cout<<"/control/alias "<<"Ion_Z_val"<<" "<<ion_z_val<<endl;
	    fout<<"/control/alias "<<"Ion_Z_val"<<" "<<ion_z_val<<endl;
	  }else{
	    cout<<value<<" / " <<translate(value)<<" existiert nicht."<<endl;	
	    fout<<"/control/alias SourceType "<<value<<endl;
	    
	  }
	  
	}else if(strcmp(labels[i]->GetText()->GetString(),"RepeatNr")==0){
	  string s(value);
	  stringstream str;
	  str<<value;
	  double repeatNr=0;
	  str >> repeatNr;
	  double deltaPhi = 360/repeatNr;
	  //cout<<deltaPhi<<endl;
	  
	  cout<<"/control/alias CrystalPhiStart  0.0 deg"<<endl;
	  fout<<"/control/alias CrystalPhiStart  0.0 deg"<<endl;
	  
	  cout<<"/control/alias CrystalDeltaPhi "<<setprecision(2)<<deltaPhi<<" deg"<<endl;
	  fout<<"/control/alias CrystalDeltaPhi "<<setprecision(2)<<deltaPhi<<" deg"<<endl;
	  
	  
	  cout<<"/control/alias "<<labels[i]->GetText()->GetString()<<" "<<value<<endl;
	  fout<<"/control/alias "<<labels[i]->GetText()->GetString()<<" "<<value<<endl;
	  
	}else if(strcmp(labels[i]->GetText()->GetString(),"UsedMacro")==0){
	  /*Do nothing*/
	}
	else{
	  cout<<"/control/alias "<<labels[i]->GetText()->GetString()<<" "<<value<<endl;
	  fout<<"/control/alias "<<labels[i]->GetText()->GetString()<<" "<<value<<endl;
	}		
      }
    }
    else{
      cout<<"No parameter selected for "<<labels[i]->GetText()->GetString()<<endl;
    }
  } // for .. num_Combo
  fout.close();
}


void GateConfiguration::Save(){	
	

	const char* tmpName="Spectro.tmp";
	ofstream fout(tmpName);
	int select=-1;
	const char* value;
	TGLBEntry *entry;

	
	for (int i=0; i<numCombo; i++) {
	  //cout << numCombo << " " << border << endl;
	  if(i==border){
	    fout<<"-"<<endl;//SourceType verschwindet, wenn man nicht checkt, also nur bei NumCobo = border
	    
	  }
	  
	  fout<<labels[i]->GetText()->GetString()<<":";
	  if(!fCombo[i]->IsTextInputEnabled()){
	    entry=fCombo[i]->GetSelectedEntry();
	    //der ausgewählte eintrag, der an den Anfang geschrieben werden soll
	    if(entry){
	      value =((TGTextLBEntry*)entry)->GetText()->GetString();//string des Eintrags
	      
	      fout<<value<<";";
	    }
	    select=fCombo[i]->GetSelected();
	    for( int j=1; j<=fCombo[i]->GetNumberOfEntries();j++){
	      if(j!=select){
		fCombo[i]->Select(j);
		entry=fCombo[i]->GetSelectedEntry();
		value =((TGTextLBEntry*)entry)->GetText()->GetString();
		fout<<value<<";";
	      }
	    }
	  }
	  else{//es wird nur 1x geschrieben, danach speichert nichts neues mehr
	    fout<<"?;";
	    //das aktuell (im EingabeFeld) geschriebene geht verloren, wenn schon ein eintrag existiert
	    entry=fCombo[i]->GetSelectedEntry();
	    if(entry){
	      //cout<<"Entry: "<<((TGTextLBEntry*)entry)->GetText()->GetString()<<endl;
	      //cout<<((TGTextLBEntry*)entry)->GetText()->GetString()<<";"<<endl;
	      fout<<((TGTextLBEntry*)entry)->GetText()->GetString()<<";";
	      
	      
	      select=fCombo[i]->GetSelected();
	      for( int j=1; j<=fCombo[i]->GetNumberOfEntries();j++){
		if(j!=select){
		  fCombo[i]->Select(j);
		  entry=fCombo[i]->GetSelectedEntry();
		  if(entry){
		    value =((TGTextLBEntry*)entry)->GetText()->GetString();
		    fout<<value<<";";
		  }
		}
	      }
	    }
	    
	  }
	  fout<<endl;
	  fCombo[i]->Select(select);
	}
	if(numCombo<=border)
	  fout<<"-"<<endl;
	
	ifstream configIn(config);
	string line;
	for(int k=0;k<=border;k++){
	  getline(configIn, line);
	}
	int dp=-1;
	bool isUsed=false;
	while(getline(configIn, line)){	
	  dp=line.find(":");
	  isUsed=false;
	  for(int i=0;i<numCombo;i++){
	    if(strcmp(line.substr(0,dp).c_str(),labels[i]->GetText()->GetString())==0)
	      isUsed = true;
	    //cout<<line.substr(0,dp)<<"     "<<labels[i]->GetText()->GetString()<<"   "<<isUsed<<endl;
	  }
	  if(!isUsed)
	    fout<<line<<endl;
	}
	
	configIn.close();
	fout.close();
	
	ifstream In(tmpName);
	ofstream out(config);
	while(getline(In,line))
	  out<<line<<endl;
	In.close();
	out.close();
	
}

void GateConfiguration::searchFile(const char* file){
  int left, right;
  ifstream fin(file);
  string temp,name;
  while(getline(fin,temp)){
    if(temp[0]!='#'){
      left = temp.find("{");
      right= temp.find("}");	
      while(left!=-1 && right !=-1){
	
	//cout<<temp.substr(left+1,right-left-1)<<endl;
	name = temp.substr(left+1,right-left-1);
	if(strcmp(name.c_str(),"Ion_Z_val") && strcmp(name.c_str(),"Ion_A_val"))
	  insertLabel(name);
	//problem: im hauptmacro werden schon fertige *.macs ignoriert 
	//werden jetzt von Hand angegeben, sollte aber funktionieren
	//vielleicht in TXT-File auslagern? TODO 
	left = temp.find("{",left+1);
	right= temp.find("}",right+1);
      }	
    }
  }
  fin.close();
  
  
}

void GateConfiguration::checkForDependencies(){
		
  string line;
  const char* value;
  char* file;
  
  for (int i=0; i<numCombo; i++) {
    
    if (fCombo[i]->GetSelected()!=-1) {
      
      TGLBEntry *entry=fCombo[i]->GetSelectedEntry();
      value =((TGTextLBEntry*)entry)->GetText()->GetString();
      while(*value==' ') value++; 

      //cout << "value " << value << endl;
      if(*value=='\0') value--;//sonst fehler bei leeren Strings
      
      
      if(strcmp(labels[i]->GetText()->GetString(), "Type in isotope, e.g. Na22 (press enter)")==0){
	file=(char*)malloc(strlen(value)+4+4+1);//+".mac" und + "ion_" und +"\0"
	strcpy(file,"ion_");
	strcat(file,(value));
      }else if(strcmp(labels[i]->GetText()->GetString(), "SourceType")==0){
	file=(char*)malloc(strlen(value)+8+4+1);
	strcpy(file,"sources_");
	strcat(file,(value));
	
      }
      else{
	file=(char*)malloc(strlen(value)+1+4+1);
	strcpy(file,(value));
      }
      
      strcat(file,".mac");
      //cout<<file<<endl;
      searchFile(file);
      
      
      free(file);
    }
    
    
    
  }
  for(unsigned int l=0;l<sizeof(additional)/sizeof(additional[0]);l++){
    searchFile(additional[l].c_str());
  }
  
}

void GateConfiguration::DoExit(){
  //gApplication->Run("Gate Gamma_Spectro.mac");   //does not work
   Printf("End of Configuration");
   gApplication->Terminate(0);
}

void GateConfiguration::showDetails(){//Fehler: bei der ersten eingabe wird das oberste Element verwendet FIXME
  
  for (int i=0; i<numCombo; i++) {
    if (fCombo[i]->GetSelected()!=-1) {
      TGLBEntry *entry=fCombo[i]->GetSelectedEntry();
      const char* value =((TGTextLBEntry*)entry)->GetText()->GetString();
      
      if(strcmp(labels[i]->GetText()->GetString(),"Type in isotope, e.g. Na22")==0){
	if(isElement(value)){
	  //auf Konsole ausgeben, was in der datei steht
	  TString s="RadioactiveDecay3.3/";
	  
	  s+=translate(value);
	  cout<<s.Data()<<endl;
	  ifstream fin(s.Data());
	  string temp;
	  while(getline(fin,temp)){
	    
	    cout<<temp<<endl;
	    
	  }
	  fin.close();
	}
	
      }
    }
  }
}

GateConfiguration::GateConfiguration(const TGWindow *p, UInt_t w, UInt_t h, char* conf) :
  TGMainFrame(p, w, h)
{	
  //vielleicht doch besser in txt-Datei auslagern?
  exceptions.push_back("CrystalPhiStart");
  exceptions.push_back("CrystalDeltaPhi");
  exceptions.push_back("UsedMacro");
  
  
  additional.push_back("phantom.mac");
  additional.push_back("physics.mac");
  additional.push_back("digitizer.mac");
  
  
  config=conf;//name der konfigurationsdatei
  numCombo=0;// anzahl der menuepunkte
  
  
  string temp;
  ifstream fin(config);
  
  while(getline(fin,temp)){
    if (!temp.empty()) {
      numCombo++;
      
    }
  }
  
  if (temp!="") {
    numCombo++;
  }
  //bis hier: erhoehen der numCombo auf die anzahl der menues
  fin.close();
  
  //hframes= new TGHorizontalFrame*[numCombo];
  //fCombo = new TGComboBox*[numCombo];	
  //labels = new TGLabel*[numCombo];
  
  fin.open(config);
  
  for (int i=0; i<numCombo; i++) {
    int numParameters=0;
    int found=0;
    getline(fin,temp);
    if(temp[0]=='-'){
      numCombo=i;
      border=i;
      break;
    }
    
    while(found!=-1){
      found=temp.find(";",found+1);
      numParameters++;
    };
    numParameters--;
    
    found=temp.find(":");//Trennzeichen nach menuepunkt
    char al[100];//name des menuepunktes, in der naechsten for schleife fuer parameter
    
    hframes.push_back(new TGHorizontalFrame(this, 350, 20, kLHintsExpandX));
    fCombo.push_back(new TGComboBox(hframes[i], 100));
    temp.copy(al,found,0);
    al[found]='\0';
    labels.push_back(new TGLabel(hframes[i],new TGString(al)));
    used.push_back(new string(al));
    fCombo.at(i)->EnableTextInput(false);
    
    for (int j=0; j<numParameters; j++) {
      
      int start=found+1;
      found=temp.find(";",start);//Trennzeichen nach einzelner option, muss auch am ende einer zeile stehen
      temp.copy(al,found-start,start);
      al[found-start]='\0';
      if(al[0] == '?')
	fCombo[i]->EnableTextInput(true);
      else
	fCombo[i]->AddEntry(al, j+1);
      
    }
    if(fCombo[i]->IsEnabled())
      fCombo.at(i)->Select(1);
    //		fCombo[i]->EnableTextInput(true);
    //		fCombo[i]->EnableTextInput(false);		
    fCombo.at(i)->Resize(300, 20);	
    hframes.at(i)->AddFrame(labels.at(i),new TGLayoutHints(kLHintsExpandX, 5, 5, 3, 4));
    hframes.at(i)->AddFrame(fCombo.at(i), new TGLayoutHints(kLHintsExpandX , 5, 5, 5, 5));
    AddFrame(hframes.at(i), new TGLayoutHints(kLHintsExpandX, 2, 2, 5, 1));		
  } //end:for
  
  // Create a horizontal frame containing button(s)
  TGHorizontalFrame *hframe = new TGHorizontalFrame(this, 350, 20, kFixedWidth);
  
  TGTextButton *generate = new TGTextButton(hframe, "&Generate configuration.mac ");
  generate->Connect("Pressed()", "GateConfiguration", this, "GenerateConfigFile()");
  hframe->AddFrame(generate, new TGLayoutHints(kFixedWidth | kLHintsCenterX, 5, 5, 3, 4));
	
  TGTextButton *save = new TGTextButton(hframe, "&Save ");
  save->Connect("Pressed()", "GateConfiguration", this, "Save()");
  hframe->AddFrame(save, new TGLayoutHints(kFixedWidth | kLHintsCenterX, 5, 5, 3, 4));
  
  TGTextButton *check = new TGTextButton(hframe, "&Check");
  check->Connect("Pressed()", "GateConfiguration", this, "checkForDependencies()");
  hframe->AddFrame(check, new TGLayoutHints(kFixedWidth | kLHintsCenterX, 5, 5, 3, 4));
  
  TGTextButton *details = new TGTextButton(hframe, "&Details");
  details->Connect("Pressed()", "GateConfiguration", this, "showDetails()");
  hframe->AddFrame(details, new TGLayoutHints(kFixedWidth | kLHintsCenterX, 5, 5, 3, 4));
  
  TGTextButton *exit = new TGTextButton(hframe, "&Exit ");
  exit->Connect("Pressed()", "GateConfiguration", this, "DoExit()");	
  hframe->AddFrame(exit, new TGLayoutHints(kFixedWidth | kLHintsCenterX, 5, 5, 3, 4));
  
  
  
  
  AddFrame(hframe, new TGLayoutHints(kLHintsExpandX, 2, 2, 5, 1));
  
  // Set a name to the main frame   
  SetWindowName("EduGate Gamma_Sphere Configuration");
  MapSubwindows();
  
  // Initialize the layout algorithm via Resize()
  Resize(GetDefaultSize());
  
  // Map main frame
  MapWindow();
  //  fListBox->Select(1);
}

GateConfiguration::~GateConfiguration()
{
   // Clean up main frame...
  Cleanup();	
}



void GenerateGateConfiguration(char* conf)
{
   // Popup the GUI...
   GateConfiguration *GammaCamera= new GateConfiguration(gClient->GetRoot(), 400, 200, conf);

}
