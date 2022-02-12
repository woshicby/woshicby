#include <stdio.h>
long long a(long long a){
	long long b=a;
	long long count=0;
	while(b!=0){
		b/=10;
		count++;
	}
	b=a;
	long long sum=0;
	while(b!=0){
		long long c=b%10;
		b/=10;
		long long d=c;
		long long j=1;
		for(j=1;j<count;j++){
			c*=d;
		}
		sum+=c;
	}
	if(sum==a){
		return a;
	}
}
int main(){
	long long i=1;
	while(1){
		if(i==a(i)){
			printf("%ld\n",i);
		}
		i++;
	}
	return 0;
}