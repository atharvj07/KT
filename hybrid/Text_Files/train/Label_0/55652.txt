import java.awt.geom.*;
import java.io.*;
import java.util.*;


public class Main {
	//2041 start
	
	class E implements Comparable<E>{
		char name;
		int min, max, sum, count;
		public E(char name) {
			this.name = name;
			min = 1 << 24;
			max = 0;
			sum = 0;
			count = 0;
		}
		
		private void calc(int num){
			sum += num;
			min = Math.min(min, num);
			max = Math.max(max, num);
			count++;
		}
		public int compareTo(E o) {
			if(this.name < o.name) return -1;
			if(this.name > o.name) return 1;
			return 0;
		}
	}
	
	class D implements Comparable<D>{
		String name;
		int pay, gain;
		public D(String name, int pay, int gain) {
			this.name = name;
			this.pay = pay;
			this.gain = gain;
		}
		public int compareTo(D o) {
			return this.name.compareTo(o.name);
		}
		@Override
		public String toString() {
			return name + " " + pay + " " + gain;
		}
	}
	
	class C{
		String s;
		int digit;
		char goods;
		int value;
		public C(String s, int digit, char goods, int value) {
			this.s = s;
			this.digit = digit;
			this.goods = goods;
			this.value = value;
		}
	}
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0)break;
			HashMap<String, D> humlist = new HashMap<String, D>();
			HashMap<Character, E> goodslist = new HashMap<Character, E>();
			ArrayList<C> data = new ArrayList<Main.C>();
			for(int i =0; i < n; i++){
				
				String name = sc.next();
				String str = sc.next();
				int digit = 0;
				if(str.equals("SELL")) digit = 1;
				else digit = -1;
				char goods= sc.next().charAt(0);
				int value = sc.nextInt();
				humlist.put(name, new D(name,0,0));
				goodslist.put(goods, new E(goods));
				data.add(new C(name, digit, goods, value));
			}
			
			ArrayList<C> record = new ArrayList<Main.C>();
			for(int i = 0; i < n;i++){
				C now = data.get(i);
				if(now.digit > 0){
					//sell
					int max = 0;
					int ind = -1;
					for(int j = 0; j < record.size(); j++){
						C nowj = record.get(j);
						if(nowj.digit < 0 && ! now.s.equals(nowj.s) && now.goods == nowj.goods){
							if(nowj.value > max){
								max = nowj.value;
								ind = j;
							}
						}
					}
					if(ind!= -1){
						C buyer = record.get(ind);
						if(buyer.value < now.value){
							record.add(now);
						}
						else{
							int res = (buyer.value + now.value) / 2;
							D a = humlist.get(now.s);
							a.gain = a.gain + res;
							D b = humlist.get(buyer.s);
							b.pay = b.pay + res;
							humlist.put(now.s, a);
							humlist.put(buyer.s, b);
							record.remove(ind);
							E c = goodslist.get(now.goods);
							c.calc(res);
							
						}
					}
					else{
						record.add(now);
					}
				}
				else{
					//buy
					int min = 1 << 24;
					int ind = -1;
					for(int j = 0; j < record.size(); j++){
						C nowj = record.get(j);
						if(nowj.digit > 0 && ! now.s.equals(nowj.s) && now.goods == nowj.goods){
							if(nowj.value < min){
								min = nowj.value;
								ind = j;
							}
						}
					}
					if(ind!= -1){
						C seller = record.get(ind);
						if(now.value < seller.value){
							record.add(now);
						}
						else{
							
							int res = (seller.value + now.value) / 2;
							D a = humlist.get(now.s);
							a.pay = a.pay + res;
							D b = humlist.get(seller.s);
							b.gain = b.gain + res;
							humlist.put(now.s, a);
							humlist.put(seller.s, b);
							record.remove(ind);
							E c = goodslist.get(now.goods);
							c.calc(res);
						}
					}
					else{
						record.add(now);
					}
				}
			}
			
			ArrayList<E> goods = new ArrayList<E>();
			ArrayList<D> hum = new ArrayList<Main.D>();
			for(String key: humlist.keySet()){
				hum.add(humlist.get(key));
			}
			
			for(char key: goodslist.keySet()){
				goods.add(goodslist.get(key));
			}
			Collections.sort(hum);
			Collections.sort(goods);
			
			for(E res: goods){
				if(res.count == 0) continue;
				System.out.println(res.name + " " + res.min + " " + (res.sum / res.count) + " " + res.max);
			}
			System.out.println("--");
			for(D res: hum){
				System.out.println(res);
			}
			System.out.println("----------");
		}
	}

	public static void main(String [] args){
		new Main().doit();
	}
}