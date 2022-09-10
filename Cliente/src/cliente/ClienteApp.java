package cliente;

import java.io.IOException;
import java.util.Scanner;

public class ClienteApp {

	public static void main(String[] args) throws IOException {
		Cliente c = new Cliente();
		Scanner sc = new Scanner(System.in);
		int op = 0;
		while(op!=8) {
			System.out.println("\nMenu\n1.Adicionar usuário\n2.Listar usuários cadastrados\n3.Alterar dados de um usuário\n4.Visualizar dados de um usuário\n5.Alterar senha de usuário\n6.Verificar se a senha está correta\n7.Remover usuário\n8.Sair");
			op = Integer.parseInt(sc.nextLine());
			switch(op) {
			case 1:
				System.out.println("Digite o nome:");
				String nome = sc.nextLine();
				System.out.println("Digite o rg:");
				String rg = sc.nextLine();
				System.out.println("Digite o matricula:");
				String matricula = sc.nextLine();
				System.out.println("Digite o endereco:");
				String endereco = sc.nextLine();
				System.out.println("Digite o senha:");
				String senha = sc.nextLine();
				c.CadastraUsuario(nome, rg, matricula, endereco, senha);
				break;
			case 2:
				System.out.println("Usuarios cadastrados:\n");
				c.ListarTodos();
				break;
				
			case 3:
				System.out.println("Digite o rg do usuario que deseja alterar dados:");
				String rg1 = sc.nextLine();
				System.out.println("Digite o novo nome:");
				String novonome = sc.nextLine();
				System.out.println("Digite o novo rg:");
				String novorg = sc.nextLine();
				System.out.println("Digite a nova matricula:");
				String novamatricula = sc.nextLine();
				System.out.println("Digite o novo endereco:");
				String novoendereco = sc.nextLine();
				c.AlterarDados(rg1,novonome,novorg,novamatricula,novoendereco);
				break;
			
			case 4:
				System.out.println("Digite o rg do usuário:");
				String rgusuario = sc.nextLine();
				System.out.println("Dados do usuário:");
				c.PesquisaUsuario(rgusuario);
				break;
			
			case 5:
				System.out.println("Digite o rg do usuário:");
				String rgusuario1 = sc.nextLine();
				System.out.println("Digite a nova senha:");
				String novasenha = sc.nextLine();
				c.AlterarSenha(rgusuario1,novasenha);
				break;
				
			case 6:
				System.out.println("Digite o rg do usuário:");
				String rgdousuario = sc.nextLine();
				System.out.println("Digite a senha:");
				String senhadousuario = sc.nextLine();
				c.VerificarSenha(rgdousuario,senhadousuario);
				
				break;
			
			case 7:
				System.out.println("Digite o rg do usuário:");
				String rgdelete = sc.nextLine();
				c.RemoverUsuario(rgdelete);
				break;
			
			case 8:
				break;
				
			default:
				System.out.println("Opção inválida!");
				break;
			}
		
		}System.out.println("End of Program");
		sc.close();
	}	

}
