	import java.util.*;
	import java.util.Map.Entry;
	 
	 
	 class Main {
	//	 static int mod =  (int) (Math.pow(10,9)+7);
		 static int mod =  2019;
		 static List<ArrayList<Integer>>  list = new ArrayList<ArrayList<Integer>>();
	    public static void main(String[] args) {
	    	
	        Scanner sc = new Scanner(System.in);
	        
	        long N = sc.nextLong();
	        
			LinkedList<Integer> q = new LinkedList<Integer>();

	        long ans=0;
			q.add(0);
			q.add(0);
			while(!q.isEmpty()) {
				int now = q.poll();
				int keta = q.poll();
				long tmp = (long) (now+3*Math.pow(10, keta));
				if(tmp<=N) {
					q.add((int)tmp);
					q.add(keta+1);
				}
				tmp = (long) (now+5*Math.pow(10, keta));
				if(tmp<=N) {
					q.add((int)tmp);
					q.add(keta+1);
				}
				tmp = (long) (now+7*Math.pow(10, keta));
				if(tmp<=N) {
					q.add((int)tmp);
					q.add(keta+1);
				}
				boolean flg3=false;
				boolean flg5=false;
				boolean flg7=false;				
				while(now>0) {
					int t = now%10;
					if(t==3) {
						flg3=true;
					} else if(t==5) {
						flg5=true;
					} else if(t==7) {
						flg7=true;
					}
					now= now/10;
				}
				if(flg3==true&&flg5==true&&flg7==true)ans++;
			}
	        
	        
	    	System.out.println(ans);
	    	
	        		
	    }
	    

	}