package jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TesteBanco {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			
			Connection banco = ConnectionFactory.getConnection();
			System.out.println("Conex�o OK!");
			
		}
		catch(Exception e){
			System.out.println("Erro na Conex�o");
			System.out.println(e);
		}
	}
	
}