#include <iostream>
using namespace std;
#include <string>

class cpu{
public:
	virtual void calculate()=0;
};
class gpu{
public:
	virtual void display()=0;
};
class memory{
public:
	virtual void storage()=0;
};

class computer{
public:
	computer(cpu * CpuOfThisComputer,gpu * GpuOfThisComputer,memory * MemoryOfThisComputer){
		this->CpuOfThisComputer=CpuOfThisComputer;
		this->GpuOfThisComputer=GpuOfThisComputer;
		this->MemoryOfThisComputer=MemoryOfThisComputer;
	}
	virtual ~computer(){
		if(CpuOfThisComputer!=NULL){
			delete CpuOfThisComputer;
			CpuOfThisComputer=NULL;
		}
		if(GpuOfThisComputer!=NULL){
			delete GpuOfThisComputer;
			CpuOfThisComputer=NULL;
		}
		if(MemoryOfThisComputer!=NULL){
			delete MemoryOfThisComputer;
			MemoryOfThisComputer=NULL;
		}
	}
	int work(){
		cout<<"-----work start-----"<<endl;
		CpuOfThisComputer->calculate();
		GpuOfThisComputer->display();
		MemoryOfThisComputer->storage();
		cout<<"-----work OK-----"<<endl;
		return 0;
	}
	int test(){
		int abs=0;
		cout<<"-----test start-----"<<endl;
		if(work()!=0){
			abs=1;
		cout<<"-----test failed-----"<<endl;	
		}
		else{
			cout<<"-----test OK-----"<<endl;
		}
		return abs;
	}
private:
	cpu * CpuOfThisComputer;
	gpu * GpuOfThisComputer;
	memory * MemoryOfThisComputer;
};

class intel{
public:
	const string factory="intel";
};
class AMD{
public:
	const string factory="AMD";
};
class NVIDIA{
public:
	const string factory="NVIDIA";
};
class TOSHIBA{
public:
	const string factory="TOSHIBA";
};
class WESTDATA{
public:
	const string factory="WESTDATA";
};

class intelCpu:public intel,public cpu{
	virtual void calculate(){
		cout<<factory<<"CPU is calculating"<<endl;
	}
};
class AMDCpu:public AMD,public cpu{
	virtual void calculate(){
		cout<<factory<<"CPU is calculating"<<endl;
	}
};

class AMDgpu:public AMD,public gpu{
	virtual void display(){
		cout<<factory<<"GPU is displaying"<<endl;
	}
};
class NVIDIAgpu:public NVIDIA,public gpu{
	virtual void display(){
		cout<<factory<<"GPU is displaying"<<endl;
	}
};

class TOSHIBAMemory:public TOSHIBA,public memory{
	virtual void storage(){
		cout<<factory<<"memory is storageing"<<endl;
	}
};
class WESTDATAMemory:public WESTDATA,public memory{
	virtual void storage(){
		cout<<factory<<"memory is storageing"<<endl;
	}
};

computer& build(cpu * cpu,gpu * gpu,memory * memory){
	cout<<"-----build start-----"<<endl;
	computer * PC=new computer(cpu,gpu,memory);
	if(PC->test()!=0){
		cout<<"-----build failed-----"<<endl;
	}
	else{
		cout<<"-----build OK-----"<<endl;
	}
	return *PC;
}

int main(){
//	cpu * intelCpu1=new intelCpu;
//	gpu * NVIDIAgpu1=new NVIDIAgpu;
//	memory * TOSHIBAMemory1=new TOSHIBAMemory;
	computer PC1=build(new intelCpu,new NVIDIAgpu,new TOSHIBAMemory);
	delete &PC1;
}
