import java.io.*;

public class Main{
    public static void main(String[] args)throws IOException{
	BufferedReader r=new BufferedReader(new InputStreamReader(System.in));
	while(true){
	    String s=r.readLine();
	    String[] t=s.split(" ");
	    int[] n=new int[t.length];
	    for(int i=0;i<2;i++){
		n[i]=Integer.parseInt(t[i]);
	    }
	    if(n[0]==0 &&n[1]==0){
		System.exit(0);
	    }
	    String u=r.readLine();
	    String[] p=u.split(" ");
	    int[] ing=new int[n[1]];
	    for(int j=0;j<n[1];j++){
		ing[j]=Integer.parseInt(p[j]);
	    }
	    int[] count=new int[n[1]];
	    for(int nm=0;nm<n[1];nm++){
		count[nm]=0;
	    }
	    for(int k=0;k<n[0];k++){
		String a=r.readLine();
		String[] alpha;
		alpha=a.split(" ");
		int[] number=new int[n[1]];
		for(int l=0;l<n[1];l++){
		    number[l]=Integer.parseInt(alpha[l]);
		    count[l]+=number[l];
		}
	    }
	    int ans=0;
	    for(int q=0;q<n[1];q++){
		if(count[q]<=ing[q]){
		    ans++;
		}
	    }
	    if(ans==n[1]){
		System.out.println("Yes");
	    }else{
		System.out.println("No");
	    }
	}
    }
}