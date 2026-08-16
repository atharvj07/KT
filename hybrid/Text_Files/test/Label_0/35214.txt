
import static java.lang.Math.*;
import static java.lang.System.*;

import java.lang.reflect.Array;
import java.util.Collection;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Random;
import java.util.Scanner;

class Main {
    public static Scanner sc = new Scanner(in);
    public static Random rand=new Random();


    class Span{
    	int f,t;
    	public Span(int _f,int _t) {
    		f=_f;t=_t;
		}
    }

    public void run() {
    	while(true){
    		int s=sc.nextInt(),n=sc.nextInt(),t=sc.nextInt();
    		String day=sc.next(),time=sc.next();
    		int p=sc.nextInt(),m=sc.nextInt();
    		if(s==0)return;

    		Span[] segs=new Span[m];

    		int tt=0;
    		for(int i=0;i<m;i++){
    			segs[i]=new Span(tt,tt+s);
    			tt+=t;
    		}

    		int dspan="All".equals(day)?60*24:60*24*7;
    		int tspan="All".equals(time)?60*24:60*12;


    		if(dspan==tspan){
        		ln(String.format("%.10f",1-Math.pow(1-1.0/p,n*m)));
    			continue;
    		}

			final int S=300;
			Span[] dsegs=new Span[S];

			if(!"All".equals(day) && "Night".equals(time)){
				int stt=-dspan;
				for(int j=0;j+1<S;j+=2){
					dsegs[j]=new Span(stt,stt+60*6);
					dsegs[j+1]=new Span(stt+60*18,stt+60*24);
					stt+=dspan;
				}
			}else{
				int stt=-dspan;
				for(int j=0;j<S;j++){
					dsegs[j]=new Span(stt,stt+tspan);
					stt+=dspan;
				}
			}
    		double M=0;
    		for(int st=-max(dspan,t);st<=0;st++){

    			for(int j=0;j<S;j++){
    				dsegs[j].f++;
    				dsegs[j].t++;
    			}
    			int s1=0,s2=0;

    			int wrap=0;
    			while(s1<m){
    				if(segs[s1].f>=dsegs[s2].t)
    					s2++;
    				else{
    					if(segs[s1].f>=dsegs[s2].f && segs[s1].t<dsegs[s2].t){
    						wrap++;
    					}
    					s1++;
    				}
    			}

    			M=max(M,1-Math.pow(1-1.0/p,n*wrap));
    		}

    		ln(String.format("%.10f",M));
        }
    }
    public static void main(String[] args) {
        new Main().run();
    }


	//output lib
	static final String br = System.getProperty("line.separator");
	static final String[] asep = new String[] { "", " ", br, br + br };

	static String str(Boolean o) {
		return o ? "YES" : "NO";
	}

	//	static String str(Double o){
	//		return String.format("%.8f",o);
	//	}
	static <K, V> String str(Map<K, V> map) {
		StringBuilder sb = new StringBuilder();
		boolean isFirst = true;
		for (Entry<K, V> set : map.entrySet()) {
			if (!isFirst)
				sb.append(br);
			sb.append(str(set.getKey())).append(":").append(str(set.getValue()));
			isFirst = false;
		}
		return sb.toString();
	}

	static <E> String str(Collection<E> list) {
		StringBuilder sb = new StringBuilder();
		boolean isFirst = true;
		for (E e : list) {
			if (!isFirst)
				sb.append(" ");
			sb.append(str(e));
			isFirst = false;
		}
		return sb.toString();
	}

	static String str(Object o) {
		int depth = _getArrayDepth(o);
		if (depth > 0)
			return _strArray(o, depth);
		Class<?> c = o.getClass();
		if (c.equals(Boolean.class))
			return str((Boolean) o);
		//if(c.equals(Double.class))return str((Double)o);

		return o.toString();
	}

	static int _getArrayDepth(Object o) {
		if (!o.getClass().isArray() || Array.getLength(o) == 0)
			return 0;
		return 1 + _getArrayDepth(Array.get(o, 0));
	}

	static String _strArray(Object o, int depth) {
		if (depth == 0)
			return str(o);
		StringBuilder sb = new StringBuilder();
		for (int i = 0, len = Array.getLength(o); i < len; i++) {
			if (i != 0)
				sb.append(asep[depth]);
			sb.append(_strArray(Array.get(o, i), depth - 1));
		}
		return sb.toString();
	}

	static void pr(Object... os) {
		boolean isFirst = true;
		for (Object o : os) {
			if (!isFirst)
				out.print(" ");
			out.print(o);
			isFirst = false;
		}
	}

	static void ln() {
		out.println();
	}

	static void ln(Object... os) {
		for (Object o : os) {
			pr(o);
			ln();
		}
	}
}