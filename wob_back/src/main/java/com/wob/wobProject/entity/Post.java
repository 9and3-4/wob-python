package com.wob.wobProject.entity;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "post")
@Getter
@Setter
@ToString
@NoArgsConstructor
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "post_id")
    private Long Id;

    @Column(nullable = false)
    private String title;

    @ManyToOne
    @JoinColumn(name = "category_id", nullable = false)
    private Category category;

    @Column(nullable = false)
    private String place;

    @Column(nullable = false)
    private int people;

    @Column(nullable = false)
    private int joiners;

    private Long expectationCost;
    private String introduction;


    private LocalDateTime date;
    private LocalDateTime regDate;

    @PrePersist
    public void prePersist() {
        date = LocalDateTime.now();
        regDate = LocalDateTime.now();
    }

    @Column(nullable = false)
    private Boolean active;

    @ManyToOne
    @JoinColumn(name = "postImage_id")
    private PostImage postImage;
}