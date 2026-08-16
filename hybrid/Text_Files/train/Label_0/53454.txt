
import java.util.HashMap;
import java.util.Scanner;

public class Stone {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        sc.close();
        int l = s.length();
        HashMap<String, Boolean> hm = new HashMap<String, Boolean>();
        int count = 1;
        hm.put(s, true);
        for(int i = 1; i<l; i++)
        {
        	s = s.charAt(l-1) + s.substring(0, l-1);
        	if(!hm.containsKey(s))
        	{
        		hm.put(s, true);
        		count++;
        	}
        }
        System.out.println(count);
        
    }
    
    
}

    
    
    

