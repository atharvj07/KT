import java.util.Scanner;


class Main {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		
		Card R=new Card();
		Card G=new Card();
		Card B=new Card();//各マークの手札


		int num[]=new int[9];


		for(int k=0;k<T;k++){

			//手札を９枚配る、各マークと数字を対応させ1枚のカードとして扱う
			for(int i =0;i<9;i++){
				num[i]= scanner.nextInt();
				
			}
			
			for(int p=0;p<9;p++){
				String st=scanner.next();
				
				switch(st){
				case "R":

					R.hand[num[p]-1]=R.hand[num[p]-1]+1;

					break;

				case"G":

					G.hand[num[p]-1]=G.hand[num[p]-1]+1;

					break;

				case"B":

					B.hand[num[p]-1]=B.hand[num[p]-1]+1;

					break;

				}

			}

		if( (B.Set()+R.Set()+G.Set()) ==3){
			System.out.println(1);
		}
		else{
			System.out.println(0);
		}
		}

		scanner.close();

	}

}


class Card{

	int hand [];
	int set=0;
	Card(){
		hand=new int[9];
	}

	//set数判定メソッド

	 public int Set(){
		set=0;

		for(int i=0;i<9;i++){
			if(hand[i]>=3){
				hand[i]=hand[i]-3;//同じカードが３枚あるなら１セット追加して捨て札にする
				set=set+1;
			}
			if(i <= 6){//3連続で同じ数字があるならい１セット追加して1枚ずつ捨て札にする
				
				while(true){
					if((((hand[i] == 0) ||((hand[i+1] ==0))||(hand[i+2]==0))))
					{
						break;}
				if( ((hand[i] >= 1) &&((hand[i+1]>=1))&&(hand[i+2]>=1))){
					hand[i]=hand[i]-1;
					hand[i+1]=hand[i+1]-1;
					hand[i+2]=hand[i+2]-1;
					set=set+1;
				}
				}

			}
			
		}
		
		for(int i=0; i < 9;i++){
		hand[i]=0;	
		}
		
	return set;
}



}







