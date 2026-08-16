
import java.io.*;
import java.util.*;
public class professorgukizandtwoarray {
	public static void main(String[] args) throws Exception
	{
		InputReader in=new InputReader(System.in);
		PrintWriter pw=new PrintWriter(System.out);
		//long[] arr={-3,-2,0,1,2,4};
		//long[] tr=floorCeiling(arr,-4);
		//System.out.println(tr[0]+" "+tr[1]);
		int n=in.nextInt();
		long[] a=new long[n];
		long sa=0;
		for(int i=0;i<n;i++)
		{
			a[i]=in.nextLong();
			sa+=a[i];
		}
		int m=in.nextInt();
		long[] b=new long[m];
		long sb=0;
		for(int i=0;i<m;i++)
		{
		 
		b[i]=in.nextLong();
		sb+=b[i];
		
		}
		long diff=Math.abs(sa-sb);
		int i1=-1;
		int j1=-1;
		int i2=-1;
		int j2=-1;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				long temp1=sa-a[i]+b[j];
				long temp2=sb-b[j]+a[i];
				if(Math.abs(temp1-temp2)<diff)
				{
					diff=Math.abs(temp1-temp2);
					i1=i;
					j1=j;
				}
			}
		}
		ArrayList<pair> ar=new ArrayList<pair>();
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				pair temp=new pair(a[i]+a[j],i,j);
				ar.add(temp);
			}
		}
		Collections.sort(ar);
		int sz=ar.size();
		long[] tr=new long[sz];
		for(int i=0;i<sz;i++)
		{
			tr[i]=(ar.get(i).sum)*2l;
		}
		boolean intwo=false;
		long asum=0;
		long mm=(long)(2*1e9+1);
		if(n>=2)
		{																																		
		for(int i=0;i<m;i++)
		{
			for(int j=i+1;j<m;j++)
			{
				long sum=sa-sb+2*1l*(b[i]+b[j]);
				long[] ff=floorCeiling(tr,sum);
				if(ff[0]!=mm)
				{
					long di=Math.abs(sum-ff[0]);
					if(di<diff)
					{
						diff=di;
						intwo=true;
						asum=ff[0];
						j1=i;
						j2=j;
					}
				}
				if(ff[1]!=mm)
				{
					long di=Math.abs(sum-ff[1]);
					if(di<diff)
					{
						diff=di;
						intwo=true;
						asum=ff[1];
						j1=i;
						j2=j;
					}
				}

				
			}
		}
		}
		if(intwo)
		{
			for(int i=0;i<sz;i++)
			{
				if(tr[i]==asum)
				{
					i1=ar.get(i).i;
					i2=ar.get(i).j;
					break;
				}
			}
		}
		System.out.println(diff);
		if(i1==-1)
		{
			System.out.println(0);
		}
		else if(i2==-1)
		{
			System.out.println(1);
		}
		else
		{
			System.out.println(2);
		}
		if(i1!=-1)
		{
			System.out.println((i1+1)+" "+(j1+1));
		}
		if(i2!=-1)
		{
			System.out.println((i2+1)+" "+(j2+1));
		}
		
		
		
		
		
		pw.close();
	}
	/*static  int binaryfloor(long[] arr,int low,int high,long x)
	{
		if(x<arr[low])
		{
			return -1;
		}
		if(x>=arr[high])
		{
			return high;
		}
		//int count=0;
		while(low<=high)
		{
			int mid=low+((high-low)>>1);
			
			if(mid-1>=0 && arr[mid-1]<=x && arr[mid]>x)
			{
				return mid-1;
			}
			else if( arr[mid]<=x && arr[mid+1]>x )
			{
				return mid;
			}
			else if(arr[mid]>x)
			{
				high=mid-1;
			}
			else
			{
				low=mid+1;
			}
			
		}
		return -1;
	}
	static  int binaryceil(long[] arr,int low,int high,long x)
	{
		if(x>arr[high])
		{
			return -1;
		}
		while(low<high)
		{
			int mid=low+(high-low)/2;
			if(arr[mid]<x && arr[mid+1]>=x)
			{
				return mid+1;
			}
			else if(arr[mid]>x)
			{
				high=mid-1;
			}
			else
			{
				low=mid+1;
			}
			
		}
		return -1;
	}*/
	static long[] floorCeiling(long[] list, long x)
	{
		int lo = -1, hi = list.length;
		while(lo < hi - 1)
		{
			int mid = (lo+hi)/2;
			if(list[mid] >= x) hi = mid;
			else lo = mid;
		}
		long[] res = new long[2];
		res[0]=(long)(2*1e9+1);
		res[1]=res[0];
		if(lo > -1) res[0] = list[lo];
		if(hi < list.length) res[1] = list[hi];
		return res;
	}

	
	
	static class pair implements Comparable<pair>
	{
		long sum;
		int i,j;
		pair(long sum,int i,int j)
		{
			this.sum=sum;
			this.i=i;
			this.j=j;
		}
		@Override
		public int compareTo(pair p1) {
			return Long.compare(this.sum, p1.sum);
		}
	}
	
	
	
	
	
	
	
	 static class InputReader {

		private InputStream stream;
		private byte[] buf = new byte[8192];
		private int curChar;
		private int snumChars;
		private SpaceCharFilter filter;

		public InputReader(InputStream stream) {
			this.stream = stream;
		}

		public int snext() {
			if (snumChars == -1)
				throw new InputMismatchException();
			if (curChar >= snumChars) {
				curChar = 0;
				try {
					snumChars = stream.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (snumChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}

		public int nextInt() {
			int c = snext();
			while (isSpaceChar(c))
				c = snext();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = snext();
			}

			int res = 0;

			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = snext();
			} while (!isSpaceChar(c));

			return res * sgn;
		}
		
		public long nextLong() {
			int c = snext();
			while (isSpaceChar(c))
				c = snext();
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = snext();
			}

			long res = 0;

			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = snext();
			} while (!isSpaceChar(c));

			return res * sgn;
		}
		
		public String readString() {
			int c = snext();
			while (isSpaceChar(c))
				c = snext();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = snext();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public boolean isSpaceChar(int c) {
			if (filter != null)
				return filter.isSpaceChar(c);
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}

		public interface SpaceCharFilter {
			public boolean isSpaceChar(int ch);
		}
	}

}
