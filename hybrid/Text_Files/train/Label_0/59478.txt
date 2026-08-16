import java.io.*;
import java.util.*;
 
public class e1 {
	public static PrintWriter out;
	public static InputReader in;
	public static int minx,maxx;
	public static void sub(int x, int arr[], int p, HashSet<Integer> set){
		// int less = 0;
		ArrayList<Long> list = new ArrayList<Long>();
		int parr[] = new int[p];
		Arrays.fill(parr,0);
		for(int i=arr.length-1;i>=0;i--){
			if(arr[i]<=x)
				break;
			long ct = (long)arr.length - (long)((long)arr[i]-(long)x);
			list.add(ct);
		}
		Collections.sort(list);
		// out.println("list : "+list);
		long i = 0;
		for(long val : list){
			parr[(int)((val-i)%((long)p))]++;
			i++;
		}
		// int ct = maxx - minx + 1;
		for(i=0;i<p;i++){
			if(parr[(int)i]!=0){
				// out.println("i "+i);
				if(i==0){
					set.remove(maxx);
				}
				int val = maxx - ((int)i);
				while(val>=minx){
					set.remove(val);
					val-=p;
				}
			}
		}
		// return true;
	}
	// public static boolean valid(int x, int arr[]){
	// 	ArrayList<Integer> list=  new ArrayList<Integer>();
	// 	for(int i=arr.length-1;i>=0;i--){
	// 		if(arr[i]<=x){
	// 			less++;
	// 		}
	// 		else{
	// 			int ct = arr.length - (arr[i]-x);
	// 			list.add(ct);
	// 		}
	// 	}
	// 	if(p<=less)
	// 		return false;
	// 	Collections.sort(list);
	// 	int i = 0;
	// 	for(int val : list){
	// 		if((val-i)<=0 || (val-i)%p==0)
	// 			return false;
	// 		i++;
	// 	}
	// 	return true;
	// }
	public static void main(String[] args)throws IOException {
        in = new InputReader(System.in);
        out = new PrintWriter(System.out);
        int n = in.nextInt();
        int p = in.nextInt();
        int arr[] = new int[n];
        HashSet<Integer> set = new HashSet<Integer>();
        int mx = -1;
        for(int i=0;i<n;i++){
        	arr[i]=in.nextInt();
        	mx = Math.max(arr[i],mx);
        }
        mergesort(arr,0,n-1);
    	// ArrayList<Integer> ansList = new ArrayList<Integer>();
    	int less = 0;
    	maxx = 0; int ix = 0;
    	minx = mx;
    	for(int i=n-1;i>=0;i--){
    		minx = Math.max(minx,arr[i]);
    		if(i!=0)
    			minx--;
    	}
    	// out.println("minVal[0]: "+minVal[0]);
        for(int x=minx;x<=mx-1;x++){
        	while(ix<n && arr[ix]<=x){
        		ix++;
        	}
        	if(ix>=p){
        		break;
        	}
        	set.add(x);
        	maxx = x;
        	minx = Math.min(minx,x);
        }
        
        // out.println("set : "+set);
        if(maxx==0 || arr[0]==mx)
        {
        	out.println(0);
        	out.close();
        	return;
        }
        sub(maxx,arr,p,set);
        // out.println("set: "+set);
        // out.println(minx+" "+maxx);
        // for(int x = maxx; x>=minx; x--){
        // 	if(valid(x,arr)){
        // 		sub(x,arr,set);
        // 	}
        // }
        out.println(set.size());
        ArrayList<Integer> list = new ArrayList<Integer>(set);
        Collections.sort(list);
        for(int x : list){
        	out.print(x+" ");
        }
        out.println();
        // out.println(-1%223);
        out.close();
	}
	public static void merge(int[] arr, int first,int mid,int last){

		int a[]=new int[mid-first+1];

		int b[]=new int[last-mid];

		// int c[]=new int[mid-first+1];

		// int d[]=new int[last-mid];

		int pahela,dusra;	
		pahela=dusra=0;

		for(pahela=0;pahela<mid-first+1;pahela++)
		{
			a[pahela]=arr[first+pahela];
			// c[pahela]=indexes[first+pahela];
		} 

		for(dusra=0;dusra<last-mid;dusra++)
		{
			b[dusra]=arr[mid+1+dusra];
			// d[dusra]=indexes[mid+1+dusra];
		}

		pahela=0;
		dusra=0;
		int maha=first;

		while(pahela<mid-first+1 && dusra<last-mid)
		{
			if(a[pahela]<=b[dusra])
			{
				arr[maha]=a[pahela];
				// indexes[maha]=c[pahela];
				maha++;
				pahela++;
			}

			else
			{
				arr[maha]=b[dusra];
				// indexes[maha]=d[dusra];
				maha++;
				dusra++;
			}
		}

		while(pahela<mid-first+1)
		{
			arr[maha]=a[pahela];
			// indexes[maha]=c[pahela];
			maha++;
			pahela++;
		}

		while(dusra<last-mid){
			arr[maha]=b[dusra];
			// indexes[maha]=d[dusra];
			maha++;
			dusra++;
		}
	}
	public static void mergesort(int arr[],int first,int last)
	{
		if(first < last) {
		int mid=(first+last)/2;
		mergesort(arr,first,mid);
		mergesort(arr,mid+1,last);
		merge(arr,first,mid,last);
	}
	}
	
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

    }

}