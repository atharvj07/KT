import java.util.*;

import java.lang.*;

import java.math.*;



public class Main {

	Scanner sc = new Scanner(System.in);



	class pole {

		double x;

		double y;

		double r;

		boolean hit;

		pole(int x, int y, int r) {

			this.x = x;

			this.y = y;

			this.r = r;

		}



		pole(pole p, point org) {

			this.x = p.x - org.x;

			this.y = p.y - org.y;

			this.r = p.r;

		}

		

		void rotate(point x1){

			double nx = this.x * x1.norm().x + this.y * x1.norm().y;

			double ny = this.y * x1.norm().x - this.x * x1.norm().y;

			this.x = nx;

			this.y = ny;

			setHit(x1);

		}

		void setHit(point x1){

			double size = x1.abs();

			if(Math.abs(this.y) > this.r + 1e-7 ){ // ~ªÚµÈ¢

				hit = false;

				return;

			}

			if(Math.abs(Math.abs(this.y) - this.r) < 1e-7 ){ // ~ªÚ·é

				if(this.x > 0 && this.x < size){

					hit = true;

				}else{

					hit = false;

				}

				return;

			}

			// ~ªðíéÆ O½ûIÉ±¤

			double amari = Math.sqrt(this.r*this.r - this.y*this.y);

			double x_1 = this.x - amari;

			double x_2 = this.x + amari;

			if(x_1 > 0 && x_1 < size){

				hit = true;

			}else if(x_2 > 0 && x_2 < size){

				hit = true;

			}else{

				hit = false;

			}

		}

	}



	class point {

		double x;

		double y;



		point(int x, int y) {

			this.x = x;

			this.y = y;

		}



		point(point p, point org) {

			this.x = p.x - org.x;

			this.y = p.y - org.y;

		}

		

		double abs(){

			return Math.sqrt(this.x*this.x+this.y*this.y);

		}

		point norm(){

			point ret = new point(0,0);

			ret.x = this.x/abs();

			ret.y = this.y/abs();

			return ret;

		}

	}



	void run() {

		for (;;) {

			int n = sc.nextInt();

			if (n == 0) {

				break;

			}

			pole[] p = new pole[n];

			for (int i = 0; i < n; i++) {

				p[i] = new pole(sc.nextInt(), sc.nextInt(), sc.nextInt());

			}

			int m = sc.nextInt();

			for (int j = 0; j < m; j++) {



				point taro_temp = new point(sc.nextInt(), sc.nextInt());

				point oni_temp = new point(sc.nextInt(), sc.nextInt());



				pole[] p2 = new pole[n];

				point oni = new point(oni_temp, taro_temp);

				boolean bra = false;

				for (int i = 0; i < n; i++) {

					p2[i] = new pole(p[i], taro_temp);

					p2[i].rotate(oni);

					if(p2[i].hit){

						System.out.println("Safe");

						bra = true;

						break;

					}

				}

				if(bra){

					continue;

				}

				System.out.println("Danger");				

			}

		}

	}



	public static void main(String[] args) {

		Main m = new Main();

		m.run();

	}

}