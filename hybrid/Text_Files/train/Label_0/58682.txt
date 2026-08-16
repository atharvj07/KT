import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		int n=Integer.parseInt(in.next());
		List<goods> ls=new ArrayList<>();
		for(int i=0;i<n;i++){
			int v=Integer.parseInt(in.next()),w=Integer.parseInt(in.next());
			char t=in.next().charAt(0);
			long d=Long.parseLong(in.next());
			String str=in.next();
			ls.add(new goods(v,w,t,d,str));
		}
		ls.sort(Comparator.comparing(goods::getValue)
				.thenComparingInt(goods::getWeight)
				.thenComparing(goods::getType)
				.thenComparingLong(goods::getDate)
				.thenComparing(goods::getName));
		
		for(int i=0;i<n;i++){
			goods g=ls.get(i);
			System.out.println(g.value+" "+g.weight+" "+g.type+" "+g.date+" "+g.name);
		}
	}

}

class goods{
	int value,weight;
	char type;
	long date;
	String name;
	
	goods(int v,int w,char t,long d,String str){
		value=v;
		weight=w;
		type=t;
		date=d;
		name=str;
	}
	
	int getValue(){
		return value;
	}
	
	int getWeight(){
		return weight;
	}
	
	char getType(){
		return type;
	}
	
	long getDate(){
		return date;
	}
	
	String getName(){
		return name;
	}
}
