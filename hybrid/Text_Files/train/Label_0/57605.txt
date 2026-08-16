import java.util.*;
import java.util.function.*;

class Monoid<T,R> implements BiFunction<T,T,R>{
	T					identity;
	BiFunction<T,T,R>	f;
	public Monoid(T identity,BiFunction<T,T,R> f){
		this.identity=identity;
		this.f=f;
	}
	@Override
	public R apply(T t,T u){
		return f.apply(t,u);
	}
}

class LazySegmentTree<T,A>{

	private T[]	array;
	private A[]	lazy;
	int			size;
	private int	highestbit,len[];

	/**
	 * a+0=a
	 * a+(b+c)=(a+b)+c
	 */
	private Monoid<T,T>				merger;
	/**
	 * (v,lazy)->v
	 */
	private BiFunction<T,A,T>		applyer;
	/**
	 * (apply,apply)->apply
	 */
	private Monoid<A,A>				unifyer;
	/**
	 * (v,lazy)->v
	 */
	private BiFunction<A,Integer,A>	multiplier;

	LazySegmentTree(int size,
			Monoid<T,T> merger,
			BiFunction<T,A,T> applyer,
			Monoid<A,A> unifyer,
			BiFunction<A,Integer,A> multiplier){
		this.size=size;
		this.highestbit=Integer.highestOneBit(size);
		this.merger=merger;
		this.applyer=applyer;
		this.unifyer=unifyer;
		this.multiplier=multiplier;
		initArray();
		Arrays.fill(array,merger.identity);
		Arrays.fill(lazy,unifyer.identity);
		for(int i=len.length-1;i>=0;--i)
			len[i]=i>=size?1:len[i<<1]+len[i<<1|1];
	}
	@SuppressWarnings("unchecked")
	private void initArray(){
		array=(T[])new Object[size*2];
		lazy=(A[])new Object[size*2];
		len=new int[size*2];
	}

	private void set(int i,A laz){
		array[i]=applyer.apply(array[i],
				multiplier.apply(laz,len[i]));
		if(i<size)
			lazy[i]=unifyer.apply(lazy[i],laz);
	}

	/**
	 * [l, r)
	 */
	void apply(int l,int r,A value){
		int l0=l+=size,r0=r+=size;
		for(;l<r;l>>=1,r>>=1){
			if((l&1)>0) set(l++,value);
			if((r&1)>0) set(--r,value);
		}
		updateParents(l0);
		updateParents(r0-1);
	}
	private void updateParents(int p){
		while(p>1){
			p>>=1;
			array[p]=applyer.apply(
					merger.apply(array[p<<1],array[p<<1|1]),
					multiplier.apply(lazy[p],len[p]));
		}
	}

	/**
	 * [l, r)
	 */
	T query(int l,int r){
		T res=merger.identity;
		spreadLazy(l+=size);
		spreadLazy((r+=size)-1);
		for(;l<r;l>>=1,r>>=1){
			if((l&1)>0) res=merger.apply(res,array[l++]);
			if((r&1)>0) res=merger.apply(res,array[--r]);
		}
		return res;
	}
	private void spreadLazy(int p){
		for(int s=highestbit;s>0;s>>=1){
			int i=p/s;
			if(!unifyer.identity.equals(lazy[i])){
				set(i<<1,lazy[i]);
				set(i<<1|1,lazy[i]);
				lazy[i]=unifyer.identity;
			}
		}
	}
}

class Main{
	public static void main(String[] $){
		Scanner s=new Scanner(System.in);
		int n=s.nextInt(),q=s.nextInt();
		Monoid<Long,Long> m=new Monoid<>(0L,Long::sum);
		LazySegmentTree<Long,Long>seg=new LazySegmentTree<>(n,m,m,m,(l,i)->l*i);
		for(int i=0;i<q;++i) {
			if(s.nextInt()==0)
				seg.apply(s.nextInt()-1,s.nextInt(),s.nextLong());
			else
				System.out.println(seg.query(s.nextInt()-1,s.nextInt()));
		}
	}
}
