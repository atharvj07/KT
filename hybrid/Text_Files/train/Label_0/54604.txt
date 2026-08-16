import java.util.*;

class Main{

    void solve(){
	Scanner sc = new Scanner(System.in);

	while(true){
	    int a = sc.nextInt();
	    int b = sc.nextInt();
	    if(a==0 && b==0) break;

	    ArrayList<Integer> a1 = new ArrayList<Integer>();
	    ArrayList<Integer> b1 = new ArrayList<Integer>();
	    for(int i=1; i*i<=a; i++){
		if(a%i==0) a1.add(i);
	    }
	    for(int i=1; i*i<=b; i++){
		if(b%i==0) b1.add(i);
	    }

	    int min = Integer.MAX_VALUE;
	    int[] data = new int[4];
	    int square = 0;
	    for(int i=0; i<a1.size(); i++){
		for(int j=0; j<b1.size(); j++){
		    data[0] = a1.get(i);
		    data[1] = a/a1.get(i);
		    data[2] = b1.get(j);
		    data[3] = b/b1.get(j);
		    Arrays.sort(data);
		    square = (data[1]-data[0])*(data[1]-data[0])+(data[2]-data[1])*(data[2]-data[1])+(data[3]-data[2])*(data[3]-data[2]);
		    min = Math.min(min,square);
		}
	    }

	    System.out.println(min);
	}
    }

    public static void main(String[] args){
	new Main().solve();
    }
}