import java.util.*;


class Main{
	public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int A = sc.nextInt();
	int B = sc.nextInt();
	int sum = 0;
	for( int i =1; i < N+1 ; ++i){
    	if((sumup(i)>= A)&&(sumup(i)<=B)){
        sum += i;
        }
    }
    System.out.println(sum);
      
    }
  	public static int sumup(int x){
  	int sum = 0;
	while(x>0){
    	sum += x%10;
    	x = x/10;
    }
    return sum;
    }
  
  
}