package com.example.city36

import android.content.Intent
import android.os.Bundle
import android.support.design.widget.BottomNavigationView
import android.support.v7.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_news.*

class NewsActivity : AppCompatActivity() {

    private val mOnNavigationItemSelectedListener = BottomNavigationView.OnNavigationItemSelectedListener { item ->
        when (item.itemId) {
            R.id.navigation_home -> {
                val intent = Intent(this, NewsActivity::class.java).apply {

                }
                startActivity(intent)
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_map-> {
                val intent = Intent(this, MapActivity::class.java).apply {

                }
                startActivity(intent)
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_poll -> {
                val intent = Intent(this, PollActivity::class.java).apply {

                }
                startActivity(intent)
                return@OnNavigationItemSelectedListener true
            }
        }
        false
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_news)

        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener)
    }
}
