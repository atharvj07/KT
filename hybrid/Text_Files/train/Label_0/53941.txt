import java.util.*;

public class Solution
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    int solution=0;
	    Scanner scanner = new Scanner(System.in);
	    int num_rooms = scanner.nextInt();
	    for(int i=0; i<num_rooms; i++){
	        int living = scanner.nextInt();
	        int max_capacity = scanner.nextInt();
	        
	        if(max_capacity-living >=2){
	            solution +=1;
	        }
	    }
	    
	    System.out.println(solution);
	}
}
