import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main{

	public static void main(String args[]){
		new Main().mainrun();
	}

	Scanner scan;
	private int N,count;
	private boolean loop,inf;
	private List<Order> OrderList;
	private Map<Integer,Integer> LineNumber,infLine;
	private HashMap<String,Integer> Var;

	private void mainrun() {
		scan = new Scanner(System.in);

		N = Integer.parseInt(scan.nextLine());
		loop = true;
		inf = false;

		OrderList = new ArrayList<>();
		LineNumber = new HashMap<>();
		Var = new HashMap<>();
		infLine = new HashMap<>();

		for(int i = 0;i < N ;i++) {
			String[] line = scan.nextLine().split(" ");
			OrderList.add(new Order(line));
			LineNumber.put(Integer.parseInt(line[0]), i);

			for(String str : line) {
				try {
					Integer.parseInt(str);
				}catch(NumberFormatException nfe){
					if(str.length() == 1) {
						Var.put(str, 0);
					}
				}
			}
		}

		for(count = 0;count < N && loop && !inf;count++) {
			Order order = OrderList.get(count);
			switch(order.act) {
			case "ADD":
			case "SUB":
				ADDSUBact(order);
				break;
			case "SET":
				SETact(order);
				break;
			case "IF":
				IFact(order);
				break;
			case "HALT":
				loop = false;
				break;
			default:
				break;
			}
		}

		if(inf) {
			System.out.println("inf");
		}else {
			Var.entrySet().stream().sorted((var1,var2)->{
				return var1.getKey().compareTo(var2.getKey());
			}).forEach((entry) -> {
				System.out.println(entry.getKey() + "=" + entry.getValue() );});
		}

		scan.close();
	}

	private void ADDSUBact(Order order) {
		int Num = Var.get(order.var2)
				+ (order.isNumber ? order.con : Var.get(order.var3))
				* (order.act.equals("ADD") ? 1 : -1) ;

		if(Num < 0 || Num >= 16) {
			loop = false;
		}else{
			Var.put(order.var1, Num);
		}
	}

	private void SETact(Order order) {
		if(order.isNumber) {
			Var.put(order.var1, order.con);
		}else {
			Var.put(order.var1, Var.get(order.var2));
		}
	}

	private void IFact(Order order) {
		if(Var.get(order.var1) == 0) {
			return;
		}

		/* 無限ループ判定 */
		if(infLine.containsKey(order.dest) && Var.get(order.var1) == infLine.get(order.dest)) {
			inf = true;
		}else {
			infLine.put(order.dest,Var.get(order.var1));
		}

		if(LineNumber.containsKey(order.dest)) {
			count = LineNumber.get(order.dest) - 1;
		}else{
			loop = false;
		}
	}
}

class Order{
	String act,var1,var2,var3;
	int con,dest,line;
	boolean isNumber = false;

	public Order(String Line[]) {
		line = Integer.parseInt(Line[0]);
		act = Line[1];

		switch(act) {
		case "ADD":
		case "SUB":
			var1 = Line[2];
			var2 = Line[3];
			try {
				con = Integer.parseInt(Line[4]);
				isNumber = true;
			}catch (NumberFormatException nfe){
				var3 = Line[4];
			}
			break;
		case "SET":
			var1 = Line[2];
			try {
				con = Integer.parseInt(Line[3]);
				isNumber = true;
			}catch (NumberFormatException nfe){
				var2 = Line[3];
			}
			break;
		case "IF":
			var1 = Line[2];
			dest = Integer.parseInt(Line[3]);
			break;
		case "HALT":
		default:
			break;
		}
	}
}
