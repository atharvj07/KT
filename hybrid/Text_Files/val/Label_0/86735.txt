import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	
	public static class Item{
		String name;
		int weight, strong;
		
		public Item(String name, int weight, int strong) {
			super();
			this.name = name;
			this.weight = weight;
			this.strong = strong;
		}
		
		public String toString(){
			return name;
		}
		
	}
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while (true) {
			final int n = sc.nextInt();
			
			if(n == 0){
				break;
			}
			
			ArrayList<Item> input = new ArrayList<Item>(n);
			
			for(int i = 0; i < n; i++){
				input.add(new Item(sc.next(), sc.nextInt(), sc.nextInt()));
			}
			
			HashSet<Item> collect = new HashSet<Item>(n);
			LinkedList<Item> list = new LinkedList<Item>();
			Stack<Integer> stack = new Stack<Integer>();
			stack.add(0);
			
			LinkedList<Item> answer = null;
			double min = Double.MAX_VALUE;
			
			LOOP:
			while(!stack.isEmpty()){
				//System.out.println(stack);
				//System.out.println("using : " +  collect);
				
				int cur = stack.pop();
				
				if(collect.size() == n){
					double g = 0;
					int up = 0;
					int down = 0;
					int count = 1;
					for(Item item : list){
						up += count * item.weight;
						down += item.weight;
						count++;
					}
					g = up / (double)down;
					
					if(min > g){
						min = g;
						answer = (LinkedList<Item>) list.clone();
					}
					collect.remove(list.removeLast());
					continue LOOP;
				}
				
				for(int i = cur; i < n; i++){
					if(!collect.contains(input.get(i))){
						int w = 0;
						for(Item item : list){
							w += item.weight;
						}
						w += input.get(i).weight;
						
						boolean flag = true;
						for(Item item : list){
							w -= item.weight;
							if(item.strong < w){
								flag = false;
								break;
							}
						}
						
						if(flag){
							collect.add(input.get(i));
							stack.push(i + 1);
							stack.push(0);
							list.add(input.get(i));
							continue LOOP;
						}
					}
				}
				
				
				//System.out.println(list);
				
				if(list.size() != 0){
					collect.remove(list.removeLast());
				}
			}
			
			for(Item item : answer){
				System.out.println(item.name);
			}
		}			

	}
}