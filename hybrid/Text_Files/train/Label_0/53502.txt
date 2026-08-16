import java.io.*;
import java.util.*;



public class main {

	public static void main(String[] args) throws IOException
	{ 
		Scanner in = new Scanner(System.in);
	      int a=in.nextInt();
	      ArrayList c = new ArrayList();
	      for (int i = 0; i < a; i++) 
	      {
			c.add(in.next());
		  }
	      boolean stop=false;
	    	  for (int i = 0; i < c.size()-1; i++) 
	    	  {
				for (int j = i+1; j < c.size(); j++) {
					for (int e = 0; e < c.get(i).toString().length(); e++) {
						for (int r = 0; r < c.get(j).toString().length(); r++) {
							if(c.get(i).toString().charAt(e)==c.get(j).toString().charAt(r))
							{
								String qq =c.get(i).toString();
								String ww =c.get(j).toString();
								String ee="111";
								if(e>r) 
									ee=qq+ww.substring(r+1);
								else
									ee=ww+qq.substring(e+1);
								for (int k = 0; k < ee.length()-1; k++) {
									for (int k2 = k+1; k2 < ee.length(); k2++) {
										if(ee.charAt(k)==ee.charAt(k2))
										{
											qq=ee.substring(0,k2);
											ww=ee.substring(k2+1,ee.length());
											ee=qq+ww;
											k=0;
											k2=0;
										}
											
									}
								}
								c.add(ee);
								c.remove(j);
								c.remove(i);
								if(c.size()>1)
								{
								i=0;
								j=1;
								e=0;
								r=1;
								}
								else 
									{stop=true;
									break;
									}
							}
							
						}
						if(stop)break;
					}
					if(stop)break;
				}
				if(stop)break;
			  }
	    String ee="";
	    for (int i = 0; i < c.size(); i++) {
			ee+=c.get(i).toString();
		}
	      System.out.println(ee);
	      
	}
	
}
