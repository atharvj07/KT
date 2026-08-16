import java.util.*;
import java.lang.Math;

public class Main
{
    static int[] d={-5,-4,-3,-1,0,1,3,4,5};
    static int[] a={0,2,5,7,8,10,13,15,16,18};
    
    public static void main(String[] args)
    {
        ArrayList<Integer> layout;
	Scanner sc=new Scanner(System.in);
	int attend=sc.nextInt();
	for(int i=0;i<attend;i++){
	    layout =new ArrayList<Integer>();
	    for(int j=0;j<4*5;j++){
		layout.add(sc.nextInt());
	    }
	    
	    System.out.println((20-2*solve(layout,0)));
	    
	}
	
    }
    static int solve(ArrayList<Integer> layout,int step)
    {
	int rem=step;
	for(int current=0;current<20;current++){
	    int currentCard =layout.get(current);
	    if(currentCard==0)break;

	    for(int k=0;k<d.length;k++){
		if((current%4==0&&k%3==0)||(current%4==3&&k%3==2)||k==4)continue;
		if((current<4&&k<3)||(current>=16&&k>5))continue;
		int next=current+d[k];
		int nextCard=layout.get(next);
		if(nextCard==0)break;
		if(currentCard==nextCard){
		    ArrayList<Integer> nextLayout=new ArrayList<Integer>(layout);
		    nextLayout.remove(Math.max(current,next));
		    nextLayout.remove(Math.min(current,next));
		    nextLayout.add(0);
		    nextLayout.add(0);
		    //  System.out.println("rem="+rem);
		    rem=Math.max(rem,solve(nextLayout,step+1));
		    if(rem==10)return 10;
		}
	    }
	}
	
	return rem;
    }  
}