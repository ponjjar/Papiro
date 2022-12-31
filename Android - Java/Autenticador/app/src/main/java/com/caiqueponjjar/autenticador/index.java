package com.caiqueponjjar.autenticador;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class index extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_index);
        Bundle dados = getIntent().getExtras();

        TextView campoUsuario = findViewById(R.id.TextoUsuario);
        String nome = dados.getString("nome");
        campoUsuario.setText("Ola, " + nome + "!");
    }

}