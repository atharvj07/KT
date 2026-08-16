
import java.lang.*;
import java.util.*;

public class Main
{
    static Scanner sc = new Scanner(System.in);
    public static void main(String args[])
    {
	int N = sc.nextInt();
	for(int c=0; c<N;c++){
	    int[][] map = new int[5][5];
	    for(int j=0; j<5; j++){
		for(int k=0; k<5; k++){
		    map[j][k] = sc.nextInt();
		}
	    }
	    int max=0;
	    
	    for(int i=0; i<5; i++){
		for(int j=0; j<5; j++){
		    
		    for(int k=i; k<5; k++){
			for(int l=j;l<5;l++){
			    boolean f = true;
			    for(int n=i; n<=k; n++){
				for(int m=j; m<=l; m++){
				    if(map[n][m]==0){
					f = false;
					break;
				    }
				}
			    }
			    if(f) max = Math.max(max, (k-i+1)*(l-j+1));
			}
		    }
		}
	    }
	    System.out.println(max);
	}	
    }
}