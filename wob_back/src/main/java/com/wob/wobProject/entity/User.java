package com.wob.wobProject.entity;


import com.wob.wobProject.constant.UserType;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "user")
@Getter
@Setter
@ToString
@NoArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "user_id")
    private Long Id;

    @Column(unique = true)
    private String email;
    private String password;

    private LocalDateTime regDate;

    @PrePersist
    public void prePersist() {
        regDate = LocalDateTime.now();
    }

    @Column(nullable = false)
    private String nickName;

    @ElementCollection
    @CollectionTable(
            name = "user_interest_sports",
            joinColumns = @JoinColumn(name = "user_id")
    )
    @Column(name = "interest_sports")
    private List<String> interestSports;

    @ElementCollection
    @CollectionTable(
            name = "user_interest_area",
            joinColumns = @JoinColumn(name = "user_id")
    )
    @Column(name = "interest_area")
    private List<String> interestArea;

    private String profile;
    private String mbti;

    @Column(nullable = false)
    private Boolean active;

    private String thirdPartyLogin;

    @Enumerated(EnumType.STRING)
    @Column(name = "user_type", columnDefinition = "ENUM('USER', 'ADMIN') DEFAULT 'USER'")
    private UserType userType;

}