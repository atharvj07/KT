import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		for(;sc.hasNext();){
			String s = sc.next();
			String t = sc.next();
			SuffixArray sa = new SuffixArray(s);
			int left=-1,right=t.length()+1;
			while(left<right-1){
				int len= (left+right)/2;
				
//				System.out.println(left+" "+right+" "+len);
				boolean f = false;
				for(int i=0;i<t.length();i++){
					if(i+len>t.length())break;
					String sub = t.substring(i,i+len);
					if(sa.contain(sub)){
						f=true;
						break;
					}
				}
				if(f){
					left=len;
				}
				else{
					right=len;
				}
					
			}
			System.out.println(left);			
		}

	}

	static class SuffixArray {
		int n,k=1;
		Integer[] sa,rank,tmp;
		String s;

		SuffixArray(String _s) {
			s=_s;
			n = s.length();
			String[] S = new String[n+1];
			S[n]="";
			for(int i=n-1;i>=0;i--){
				S[i] = s.charAt(i)+S[i+1];
			}
			rank=new Integer[n+1];
			sa=new Integer[n+1];
			tmp=new Integer[n+1];
			for(int i=0;i<n;i++){
				sa[i]=i;
				rank[i]=(int) s.charAt(i);
			}
			sa[n]=n;
			rank[n]=-1;

			for(k=1;k<=n;k<<=1){
				Arrays.sort(sa,new Comparator<Integer>(){
					@Override
					public int compare(Integer o1, Integer o2) {
						int r1=rank[o1];
						int r2=rank[o2];
						if(r1!=r2)return (r1-r2);
						int r11=o1+k <= n ? rank[o1+k] : -1;
						int r22=o2+k <= n ? rank[o2+k] : -1;

						return (r11-r22);
					}
				});
				tmp[sa[0]]=0;
				for(int i=1;i<=n;i++){
					tmp[sa[i]]=tmp[sa[i-1]]+ (compare(sa[i-1],sa[i])!=0?1:0);
				}
				for(int i=0;i<=n;i++){
					rank[i]=tmp[i];
				}
			}
		}
		boolean contain(String t){
			return contain(s,sa,t);
		} 
		private boolean contain(String s,Integer[] sa,String t){
			int a=0,b=s.length();
			while(b-a>1){
				int c = (a+b)/2;
//				String sub = s.substring(sa[c], Math.min(sa[c]+t.length(), s.length()));
				//			System.out.println(sub);
				//			System.out.println(a+" "+c+" "+b);
				
				int com = compare(s,sa[c], Math.min(sa[c]+t.length(), s.length()),t);
//				int com = compare(s,sa[c], sa[c]+t.length()< s.length() ? sa[c]+t.length():s.length(),t);
//				if(sub.compareTo(t)<0 != com < 0){
//					System.out.println(sub.compareTo(t)+" "+com);
//					System.out.println(sa[c]+" "+sa[c]+" "+t.length()+" "+s.length());
//					System.out.println(sub+" "+t);
//				}
//				if(sub.compareTo(t)<0){
				if(com<0){
					a=c;
				}
				else{
					b=c;
				}
			}
//			return s.substring(sa[b], Math.min(sa[b]+t.length(), s.length())).compareTo(t)==0;
//			return compare(s,sa[b], sa[b]+t.length()< s.length() ? sa[b]+t.length():s.length(),t)==0;
			return compare(s,sa[b], Math.min(sa[b]+t.length(), s.length()),t)==0;
		}
		/*
		 * s.substring(i1,i2).compare(t)と同じ。メモリ節約
		 */
		private int compare(String s,int i1,int i2,String t){
//			if(true)
//				return s.substring(i1,i2).compareTo(t);
					
			for(int i=i1;i<i2;i++){
				if(i-i1>=t.length()){
					return 1;
				}
				if(s.charAt(i)!=t.charAt(i-i1)){
					return s.charAt(i)-t.charAt(i-i1);
				}
			}
			return (i2-i1)-t.length();
		}

		/*
		 * s.substring(i1,i2).compare(t.substring(j1,j2)と同じ。メモリ節約
		 */
		private int compare(String s,int i1,int i2,String t,int j1,int j2){
			int slen=i2-i1;
			int tlen=j2-j1;
			for(int i=0;i<slen;i++){
				if(i>=tlen){
					return 1;
				}
				if(s.charAt(i+i1)!=t.charAt(i+j1)){
					return s.charAt(i+i1)-t.charAt(i+j1);
				}
			}
			return slen-tlen;
		}

		private int compare(Integer o1, Integer o2) {
			int r1=rank[o1];
			int r2=rank[o2];
			if(r1!=r2)return (r1-r2);
			int r11=o1+k <= n ? rank[o1+k] : -1;
			int r22=o2+k <= n ? rank[o2+k] : -1;

			return (r11-r22);
		}

	}

}