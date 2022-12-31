package com.caiqueponjjar.autenticador;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.util.MapUtils;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    private DatabaseReference referencia = FirebaseDatabase.getInstance().getReference();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    public void moverCadastrar(View view) {
        // cria view para se cadastrar
        Intent intent = new Intent(getApplicationContext(), Cadastro.class);
        startActivity(intent);
    }

    public void logarUsuario(View view) {
        TextView campoEmail = findViewById(R.id.CampoEmailLogin);
        TextView campoSenha = findViewById(R.id.CampoSenhaLogin);
        if ((campoSenha.getText().toString().trim().length() > 0) && (campoEmail.getText().toString().trim().length() > 0)) {
            if (campoEmail.getText().toString().contains("@")) {
                DatabaseReference usuarios = referencia.child("usuarios");

                Query usuarioPesquisa = usuarios.orderByChild("email").equalTo(campoEmail.getText().toString());

                usuarioPesquisa.addValueEventListener(new ValueEventListener() {

                    @Override
                    public void onDataChange(DataSnapshot snapshot) {

                        if (snapshot.exists()) {
                            Log.i("dados:", "dados usuário:" + snapshot.toString());
                            for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
                                //verifica se o email está correto
                                if (dataSnapshot.exists()) {
                                    Usuario dadosUsuario = dataSnapshot.getValue(Usuario.class);
                                    Log.i("dados:", "campo:" + campoSenha.getText().toString());
                                    // verifica se a senha está correta
                                    if (dadosUsuario.getSenha().equals(campoSenha.getText().toString())) {
                                        // cria nova view para a pagina inicial após o login:
                                        Intent intent = new Intent(getApplicationContext(), index.class);
                                        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                                        // transfere os dados de usuário para a próxima view
                                        intent.putExtra("nome", dadosUsuario.getNome());
                                        intent.putExtra("email", dadosUsuario.getEmail());
                                        intent.putExtra("tipo", dadosUsuario.getTipo());
                                        startActivity(intent);
                                        finish();
                                    } else {
                                        // caso esteja incorreto:
                                        Toast.makeText(MainActivity.this, "Email ou Senha incorreto.", Toast.LENGTH_SHORT).show();
                                    }
                                } else {
                                    // caso esteja incorreto:
                                    Toast.makeText(MainActivity.this, "Email ou Senha incorreto.", Toast.LENGTH_SHORT).show();
                                }
                            }
                        } else {
                            Toast.makeText(MainActivity.this, "Email ou Senha incorreto.", Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onCancelled(DatabaseError error) {
                        Toast.makeText(MainActivity.this, "Email ou Senha incorreto.", Toast.LENGTH_LONG).show();
                    }
                });

            } else {
                Toast.makeText(MainActivity.this, "Email invalido", Toast.LENGTH_SHORT).show();
            }
        } else {
            Toast.makeText(MainActivity.this, "Preencha todos os campos", Toast.LENGTH_SHORT).show();
        }
    }
}