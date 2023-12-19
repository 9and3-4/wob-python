package com.wob.wobProject.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;

@Entity
@Table(name = "search")
@Getter
@Setter
@ToString
@NoArgsConstructor
public class Search {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "search_id")
    private Long Id;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    private String keyword;
}