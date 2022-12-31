package com.caiqueponjjar.autenticador;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

public class Cadastro extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cadastro);
    }

    private DatabaseReference referencia = FirebaseDatabase.getInstance().getReference();
    public void cadastrarUsuario (View view) {
        //campos do formulário:
        TextView campoEmail = findViewById(R.id.CampoEmailCadastro);
        TextView campoNome = findViewById(R.id.CampoNomeCadastro);
        TextView campoSenha = findViewById(R.id.CampoSenhaCadastro);
        TextView campoTipo = findViewById(R.id.CampoTipoCadastro);

        // filtra os dados de usuário:
        if ((campoSenha.getText().toString().trim().length() > 0) && (campoEmail.getText().toString().trim().length() > 0) && (campoNome.getText().toString().trim().length() > 0) && (campoTipo.getText().toString().trim().length() > 0)) {
            if (campoEmail.getText().toString().contains("@")) {
                DatabaseReference usuarios = referencia.child("usuarios");
                Query usuarioPesquisa = usuarios.orderByChild("email").equalTo(campoEmail.getText().toString());
                // verifica se o usuário é duplicado.
                usuarioPesquisa.addValueEventListener(new ValueEventListener() {
                                                          @Override
                                                          public void onDataChange(DataSnapshot snapshot) {
                                                              // verifica se o usuario ja foi cadastrado
                                                              boolean cadastrado = false;
                                                              if (!snapshot.exists()) {
                                                                  Usuario usuario = new Usuario();
                                                                  //adiciona um nome, tipo e senha para o usuário ao se cadastrar
                                                                  usuario.setEmail(campoEmail.getText().toString());
                                                                  usuario.setNome(campoNome.getText().toString());
                                                                  usuario.setTipo(campoTipo.getText().toString());
                                                                  usuario.setSenha(campoSenha.getText().toString());
                                                                  cadastrado = true;
                                                                  //Determina o local onde sera incrementado os dados de usuário
                                                                  usuarios.push().setValue(usuario);
                                                                  Toast.makeText(Cadastro.this, "O usuário foi cadastrado com sucesso!", Toast.LENGTH_SHORT).show();

                                                                  Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                                                                  startActivity(intent);
                                                              }else{
                                                                  if(cadastrado == false) {
                                                                       Toast.makeText(Cadastro.this, "Email de usuário ja cadastrado.", Toast.LENGTH_SHORT).show();
                                                                  }
                                                              }
                                                          }

                                                          @Override
                                                          public void onCancelled(DatabaseError error) {

                                                          }
                                                      }
                                                      );

            }else{
                Toast.makeText(Cadastro.this, "Email inválido.", Toast.LENGTH_SHORT).show();
            }
        }else{
            Toast.makeText(Cadastro.this, "Preencha todos os campos.", Toast.LENGTH_SHORT).show();
        }
    }
    public void moverLogar (View view) {
        Intent intent = new Intent(getApplicationContext(), MainActivity.class);
        startActivity(intent);
    }
}