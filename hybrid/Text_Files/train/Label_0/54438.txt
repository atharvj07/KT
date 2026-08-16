import java.util.*;

public class HelloWorld {
	public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        
      
           int t,ans=0;
           t=sc.nextInt();
           while(t>0)
           {
              
        	  int n = sc.nextInt();
        	  int a = sc.nextInt();
        	  int b = sc.nextInt();
        	  
        	  String s = sc.next();
        	  if(b>0) {
        		  ans= (a + b)*n;
        	  }
        	  else if(b==0) {
        		  ans=a*n;
        	  }else if(b<0) {
        		  int x=0;
        		  char y=s.charAt(0);
        		  for(int i=0;i<n;i++) {
        			  if(s.charAt(i)!=y && s.charAt(i)!=s.charAt(0)) {
        				  x++;
        			  }
        			  y=s.charAt(i);
        		  }
        		  ans=a*n+b*(x+1);
        	  }
        	  System.out.println(ans);
          t--;
           }
       sc.close();
	}
}