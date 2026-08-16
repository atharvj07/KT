import java.util.*;
public class Main
{
    public static int solve(List<Integer>list,int val){
        int left=0,right=list.size()-1;
        while(left<right){
            int mid=left+(right-left)/2;
            if(list.get(mid)>=val){
                right=mid;
            }else{
                left=mid+1;
            }
        }
        return left;
    }
	public static void main(String[] args) {
	    Scanner scan=new Scanner(System.in);
	    int t=scan.nextInt();
	    while(t>0){
	        int n=scan.nextInt();
	        int a[]=new int[n];
	        for(int i=0;i<n;i++){
	            a[i]=scan.nextInt();
	        }
	        Map<Integer,Integer>map=new HashMap<>();
	        for(int i=0;i<n;i++){
	            map.put(a[i],map.getOrDefault(a[i],0)+1);
	        }
	        List<Integer>list=new ArrayList<>();
	        for(int key:map.keySet()){
	            list.add(map.get(key));
	        }
	        Collections.sort(list);
	        //System.out.println(list);
	        int min=Integer.MAX_VALUE;
	        for(int i=0;i<list.size();i++){
	            int val=list.get(i);
	            int lb=solve(list,val);
	            //System.out.println(lb);
	            min=Math.min(min,n-(list.size()-lb)*(val));
	            
	        }
	        System.out.println(min);
	        t--;
	    }
	}
}