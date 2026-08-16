import java.util.Scanner;
public class Main {
	public static String sarch(int in[]){
		int i;
		//four
		for(i=1;i<4;i++){
			if(in[0]!=in[i]){
				break;
			}
		}
		if(i==4)
			return "four card";
		for(i=2;i<5;i++){
			if(in[1]!=in[i]){
				break;
			}
		}
		if(i==5)
			return "four card";
		//full house
		if(in[0]==in[1] && in[2]==in[3] && in[3]==in[4])
			return "full house";
		if(in[0]==in[1] && in[1]==in[2] && in[3]==in[4])
			return "full house";
		//straight
		for(i=1;i<5;i++){
			if(in[i-1]+1!=in[i]) break;
		}
		if(i==5) return "straight";
		if(in[0]==1 && in[1]==10 && in[2]==11 && in[3]==12 && in[4]==13){
			return "straight";
		}
		//three
		for(i=1;i<3;i++){
			if(in[0]!=in[i]){
				break;
			}
		}
		if(i==3)
			return "three card";
		for(i=2;i<4;i++){
			if(in[1]!=in[i]){
				break;
			}
		}
		if(i==4)
			return "three card";
		for(i=3;i<5;i++){
			if(in[2]!=in[i]){
				break;
			}
		}
		if(i==5)
			return "three card";
		//two pair
		if(in[0]==in[1] && in[2]==in[3])
			return "two pair";
		if(in[0]==in[1] && in[3]==in[4])
			return "two pair";
		if(in[1]==in[2] && in[3]==in[4])
			return "two pair";
		//one
		if(in[0]==in[1])
			return "one pair";
		if(in[1]==in[2])
			return "one pair";
		if(in[2]==in[3])
			return "one pair";
		if(in[3]==in[4])
			return "one pair";
		
		//null
		return "null";
	}

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int in[]=new int[5],i,j,min,tmp;
		while(sc.hasNext()){
			String str[]=sc.next().split(",");
			for(i=0;i<5;i++){
				in[i]=Integer.parseInt(str[i]);
			}
			//sort
			for(i=0;i<5;i++){
				min=i;
				for(j=i;j<5;j++){
					if(in[j]<in[min]) min=j;
				}
				tmp=in[i];
				in[i]=in[min];
				in[min]=tmp;
			}
			System.out.println(sarch(in));
		}
	}
}